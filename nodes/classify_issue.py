from llm import llm


def classify_issue(state):
    user_issue = state["user_issue"]

    prompt = f"""
You are an IT support classification assistant.

Classify the following IT issue into ONE of these categories:

- password_reset
- vpn_issue
- network_issue
- hardware_issue
- access_issue
- security_issue

IMPORTANT:

Use security_issue for:
- hacked accounts
- suspicious login activity
- phishing
- malware
- ransomware
- compromised accounts
- unauthorized access
- security breaches

Use access_issue only for:
- permission problems
- inability to access systems
- profile access issues
- shared drive access
- login access problems WITHOUT security concerns

User issue:
{user_issue}

Return ONLY the category name.
"""

    response = llm.invoke(prompt)

    issue_type = response.content.strip()

    state["issue_type"] = issue_type

    print(f"AI Classified Issue As: {issue_type}")

    return state