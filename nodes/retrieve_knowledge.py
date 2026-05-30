from utils.knowledge_loader import load_knowledge


def retrieve_knowledge(state):

    issue_type = state["issue_type"]

    knowledge_base = load_knowledge(
        issue_type
    )

    state["knowledge_base"] = knowledge_base

    return state