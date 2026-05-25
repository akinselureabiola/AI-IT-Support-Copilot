from typing import TypedDict, List


class ITSupportState(TypedDict):

    user_issue: str
    conversation_history: str
    issue_type: str
    troubleshooting_steps: List[str]
    resolution: str
    escalation_needed: bool