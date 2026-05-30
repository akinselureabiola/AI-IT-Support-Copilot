from dotenv import load_dotenv
load_dotenv()

import streamlit as st

from workflow import app
from nodes.troubleshoot import troubleshoot
from ticketing import (
    generate_ticket,
    update_ticket_status
)


st.set_page_config(
    page_title="AI IT Support Copilot",
    page_icon="💻",
    layout="wide"
)

st.title("💻 AI IT Support Copilot")

st.markdown(
    "AI-powered IT troubleshooting and escalation assistant."
)


# ==========================
# SESSION STATE
# ==========================

if "messages" not in st.session_state:
    st.session_state.messages = []

if "current_ticket" not in st.session_state:
    st.session_state.current_ticket = None

if "issue_type" not in st.session_state:
    st.session_state.issue_type = None


# ==========================
# DISPLAY CHAT HISTORY
# ==========================

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# ==========================
# CHAT INPUT
# ==========================

user_issue = st.chat_input(
    "Describe your IT issue..."
)


if user_issue:

    # Store user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_issue
        }
    )

    # Display user message
    with st.chat_message("user"):
        st.markdown(user_issue)

    # ==========================
    # BUILD CONVERSATION HISTORY
    # ==========================

    conversation_history = ""

    for msg in st.session_state.messages:

        conversation_history += (
            f"{msg['role']}: {msg['content']}\n"
        )

    # ==========================
    # INITIAL STATE
    # ==========================

    initial_state = {
        "user_issue": user_issue,
        "conversation_history": conversation_history,
        "issue_type": "",
        "knowledge_base": "",
        "follow_up_question": "",
        "troubleshooting_steps": [],
        "resolution": "",
        "escalation_needed": False
    }

    # ==========================
    # FIRST MESSAGE
    # RUN FULL GRAPH
    # ==========================

    if st.session_state.issue_type is None:

        result = app.invoke(
            initial_state
        )

        st.session_state.issue_type = (
            result["issue_type"]
        )

    # ==========================
    # FOLLOW-UP MESSAGE
    # KEEP SAME ISSUE TYPE
    # ==========================

    else:

        from utils.knowledge_loader import load_knowledge

        initial_state["issue_type"] = (
            st.session_state.issue_type
        )

        initial_state["knowledge_base"] = (
            load_knowledge(
                st.session_state.issue_type
            )
        )

        result = troubleshoot(
            initial_state
        )

        result["issue_type"] = (
            st.session_state.issue_type
        )

        result["follow_up_question"] = ""

        result["escalation_needed"] = False

    # ==========================
    # GENERATE TICKET ONCE
    # ==========================

    if st.session_state.current_ticket is None:

        ticket = generate_ticket(
            result["issue_type"],
            result["escalation_needed"]
        )

        st.session_state.current_ticket = ticket

    else:

        ticket = st.session_state.current_ticket

        ticket = update_ticket_status(
            ticket,
            user_issue
        )

        if ticket["status"] == "Resolved":

            result["resolution"] = (
                f"Thank you for confirming. "
                f"Ticket {ticket['ticket_id']} "
                f"has been marked as Resolved."
            )

        elif ticket["status"] == "Escalated":

            result["resolution"] = (
                f"Ticket {ticket['ticket_id']} "
                f"has been escalated to "
                f"{ticket['assigned_team']}."
            )

        st.session_state.current_ticket = ticket

    # ==========================
    # FOLLOW-UP QUESTION
    # ==========================

    follow_up = result.get(
        "follow_up_question",
        ""
    )

    # ==========================
    # BUILD RESPONSE
    # ==========================

    ai_response = f"""
### Issue Classification
{result['issue_type']}

### Follow-Up Question
{follow_up if follow_up else 'No follow-up question'}

### Troubleshooting Response
{result['resolution']}

### Escalation Status
{"Escalated to IT Support Team" if result["escalation_needed"] else "No escalation required"}

### Support Ticket
- Ticket ID: {ticket['ticket_id']}
- Priority: {ticket['priority']}
- Assigned Team: {ticket['assigned_team']}
- Status: {ticket['status']}
"""

    # Store assistant response
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": ai_response
        }
    )

    # Display assistant response
    with st.chat_message("assistant"):
        st.markdown(ai_response)


# ==========================
# SIDEBAR
# ==========================

with st.sidebar:

    st.header("Support Session")

    if st.session_state.issue_type:

        st.write(
            f"Current Issue Type: {st.session_state.issue_type}"
        )

    if st.session_state.current_ticket:

        st.write(
            f"Ticket ID: {st.session_state.current_ticket['ticket_id']}"
        )

    if st.button("Start New Ticket"):

        st.session_state.messages = []

        st.session_state.current_ticket = None

        st.session_state.issue_type = None

        st.rerun()