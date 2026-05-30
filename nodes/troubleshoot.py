from llm import llm
from utils.knowledge_loader import load_knowledge


def troubleshoot(state):

    user_issue = state["user_issue"]
    issue_type = state["issue_type"]
    conversation_history = state["conversation_history"]

    knowledge_base = state["knowledge_base"]

    prompt = f"""
    You are an experienced IT Support Engineer.

    Knowledge Base:
    {knowledge_base}

    Conversation History:
    {conversation_history}

    Current Issue Type:
    {issue_type}

    Latest User Message:
    {user_issue}

    Instructions:

    1. Continue troubleshooting the existing issue.
    2. Use the knowledge base as your primary source of guidance.
    3. Use previous conversation context.
    4. Do NOT repeat previous troubleshooting steps.
    5. Do NOT classify the issue again.
    6. Do NOT generate ticket information.
    7. Do NOT include headings such as:
    - Issue Classification
    - Follow-Up Question
    - Troubleshooting Recommendation
    8. Provide:
    - One troubleshooting recommendation
    - One short explanation
    9. If the knowledge base contains relevant guidance, prioritize it over general knowledge.

    Keep the response concise, professional, and practical.
    """

    response = llm.invoke(prompt)

    ai_response = response.content.strip()

    state["troubleshooting_steps"] = [ai_response]
    state["resolution"] = ai_response

    print("\nAI Troubleshooting Response:")
    print(ai_response)

    return state