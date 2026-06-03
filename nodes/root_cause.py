from llm import llm


def generate_root_cause(state):

    conversation_history = state[
        "conversation_history"
    ]

    issue_type = state[
        "issue_type"
    ]

    prompt = f"""
You are an IT Incident Manager.

Issue Type:
{issue_type}

Conversation:
{conversation_history}

Generate a concise root cause analysis.

Return only:

Issue Type:
...

Likely Cause:
...

Actions Taken:
...

Outcome:
...
"""

    response = llm.invoke(prompt)

    state["root_cause_summary"] = (
        response.content.strip()
    )

    return state