def ask_questions(state):

    issue_type = state["issue_type"]

    if issue_type == "password_reset":
        question = (
            "Have you tried resetting your password using the company portal?"
        )

    elif issue_type == "vpn_issue":
        question = (
            "Are you receiving any VPN error messages?"
        )

    elif issue_type == "email_issue":
        question = (
            "Can you send or receive emails?"
        )

    else:
        question = (
            "Can you provide more details about the issue?"
        )

    state["follow_up_question"] = question

    return state