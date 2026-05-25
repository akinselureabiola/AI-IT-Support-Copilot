from llm import llm


def troubleshoot(state):

    user_issue = state["user_issue"]
    issue_type = state["issue_type"]
    conversation_history = state["conversation_history"]

    prompt = f"""
    You are an expert IT Support Engineer helping a user troubleshoot an ongoing IT issue.

    Conversation History:
    {conversation_history}

    Latest User Message:
    "{user_issue}"

    Current Issue Classification:
    "{issue_type}"

    Your task:
    1. Understand the FULL troubleshooting context
    2. Avoid repeating previous troubleshooting already suggested
    3. Ask ONE intelligent follow-up troubleshooting question
    4. Provide ONE concise troubleshooting recommendation

    Keep responses practical, conversational, and professional.
    """

    response = llm.invoke(prompt)

    ai_response = response.content.strip()

    state["troubleshooting_steps"] = [ai_response]
    state["resolution"] = ai_response

    print("\nAI Troubleshooting Response:")
    print(ai_response)

    return state