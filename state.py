from typing import TypedDict, List


class ITSupportState(TypedDict):

    user_issue: str
    conversation_history: str
    issue_type: str
    knowledge_base: str
    follow_up_question: str
    troubleshooting_steps: List[str]
    resolution: str
    root_cause_summary: str
    escalation_needed: bool