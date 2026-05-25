from dotenv import load_dotenv
load_dotenv()

import streamlit as st

from workflow import app
from ticketing import generate_ticket


st.set_page_config(
    page_title="AI IT Support Copilot",
    page_icon="💻",
    layout="wide"
)

st.title("💻 AI IT Support Copilot")

st.markdown(
    "AI-powered IT troubleshooting and escalation assistant."
)


# Store conversation history
if "messages" not in st.session_state:
    st.session_state.messages = []


# Store active support ticket
if "current_ticket" not in st.session_state:
    st.session_state.current_ticket = None


# Display previous messages
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# Chat input
user_issue = st.chat_input("Describe your IT issue...")


if user_issue:

    # Store user message
    st.session_state.messages.append({
        "role": "user",
        "content": user_issue
    })

    # Display user message
    with st.chat_message("user"):
        st.markdown(user_issue)

    # Build conversation history
    conversation_history = ""

    for msg in st.session_state.messages:

        role = msg["role"]
        content = msg["content"]

        conversation_history += f"{role}: {content}\n"


    initial_state = {
        "user_issue": user_issue,
        "conversation_history": conversation_history,
        "issue_type": "",
        "troubleshooting_steps": [],
        "resolution": "",
        "escalation_needed": False
    }

    # Run workflow
    result = app.invoke(initial_state)

    # Generate ticket ONLY if one does not already exist
    if st.session_state.current_ticket is None:

        ticket = generate_ticket(
            result["issue_type"],
            result["escalation_needed"]
        )

        st.session_state.current_ticket = ticket

    else:

        ticket = st.session_state.current_ticket

    # Build AI response
    ai_response = f"""
### Issue Classification
{result['issue_type']}

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

    # Store AI response
    st.session_state.messages.append({
        "role": "assistant",
        "content": ai_response
    })

    # Display AI response
    with st.chat_message("assistant"):
        st.markdown(ai_response)