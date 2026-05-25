def escalate(state):

    issue_type = state["issue_type"]
    user_issue = state["user_issue"]

    critical_issues = [
        "hardware_issue",
        "security_issue"
    ]

    if issue_type in critical_issues:
        state["escalation_needed"] = True

        escalation_message = (
            f"This issue requires escalation to the IT support team: {user_issue}"
        )

        state["resolution"] += (
            "\n\nESCALATION NOTICE:\n"
            + escalation_message
        )

        print("\nESCALATION TRIGGERED")
        print(escalation_message)

    else:
        state["escalation_needed"] = False

    return state