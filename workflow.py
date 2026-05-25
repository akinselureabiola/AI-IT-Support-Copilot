from langgraph.graph import StateGraph, END

from state import ITSupportState

from nodes.classify_issue import classify_issue
from nodes.ask_questions import ask_questions
from nodes.troubleshoot import troubleshoot
from nodes.escalate import escalate


workflow = StateGraph(ITSupportState)

# Add nodes
workflow.add_node("classify_issue", classify_issue)
workflow.add_node("ask_questions", ask_questions)
workflow.add_node("troubleshoot", troubleshoot)
workflow.add_node("escalate", escalate)

# Define workflow
workflow.set_entry_point("classify_issue")

# Route after classification
def route_issue(state):

    issue_type = state["issue_type"]

    if issue_type == "security_issue":
        return "escalate"

    elif issue_type == "password_reset":
        return "ask_questions"

    elif issue_type == "network_issue":
        return "ask_questions"

    elif issue_type == "hardware_issue":
        return "ask_questions"

    else:
        return "ask_questions"


# Conditional routing
workflow.add_conditional_edges(
    "classify_issue",
    route_issue,
    {
        "ask_questions": "ask_questions",
        "escalate": "escalate"
    }
)

workflow.add_edge("ask_questions", "troubleshoot")
workflow.add_edge("troubleshoot", END)
workflow.add_edge("escalate", END)

# Compile graph
app = workflow.compile()