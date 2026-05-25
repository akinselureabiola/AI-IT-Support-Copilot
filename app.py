from dotenv import load_dotenv
import os

load_dotenv()

from workflow import app


# Ask user for issue
user_issue = input("Describe your IT issue: ")


# Initial workflow state
initial_state = {
    "user_issue": user_issue,
    "issue_type": "",
    "troubleshooting_steps": [],
    "resolution": "",
    "escalation_needed": False
}

# Run workflow
result = app.invoke(initial_state)

print("\nAI SUPPORT COPILOT")
print("-" * 40)

print(f"\nIssue Identified: {result['issue_type']}")

print("\nRecommended Support Steps:")
print(result["resolution"])

if result["escalation_needed"]:
    print("\nStatus: Escalated to IT Support Team")
else:
    print("\nStatus: Issue can likely be resolved without escalation")

print("\nThank you for using AI IT Support Copilot.")