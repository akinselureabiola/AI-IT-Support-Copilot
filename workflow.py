from langgraph.graph import StateGraph, END

from state import ITSupportState

from nodes.classify_issue import classify_issue
from nodes.retrieve_knowledge import retrieve_knowledge
from nodes.ask_questions import ask_questions
from nodes.troubleshoot import troubleshoot
from nodes.escalate import escalate


# Create workflow
workflow = StateGraph(ITSupportState)


# ==========================
# NODES
# ==========================

workflow.add_node(
    "classify_issue",
    classify_issue
)

workflow.add_node(
    "retrieve_knowledge",
    retrieve_knowledge
)

workflow.add_node(
    "ask_questions",
    ask_questions
)

workflow.add_node(
    "troubleshoot",
    troubleshoot
)

workflow.add_node(
    "escalate",
    escalate
)


# ==========================
# ENTRY POINT
# ==========================

workflow.set_entry_point(
    "classify_issue"
)


# ==========================
# ROUTING LOGIC
# ==========================

def route_issue(state):

    issue_type = state["issue_type"]

    if issue_type == "security_issue":
        return "escalate"

    return "retrieve_knowledge"


# ==========================
# CONDITIONAL ROUTING
# ==========================

workflow.add_conditional_edges(
    "classify_issue",
    route_issue,
    {
        "retrieve_knowledge": "retrieve_knowledge",
        "escalate": "escalate"
    }
)


# ==========================
# WORKFLOW PATHS
# ==========================

workflow.add_edge(
    "retrieve_knowledge",
    "ask_questions"
)

workflow.add_edge(
    "ask_questions",
    "troubleshoot"
)

workflow.add_edge(
    "troubleshoot",
    END
)

workflow.add_edge(
    "escalate",
    END
)


# ==========================
# COMPILE GRAPH
# ==========================

app = workflow.compile()