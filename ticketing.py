import random


def generate_ticket(issue_type, escalation_needed):

    ticket_id = f"INC-{random.randint(1000, 9999)}"

    priority = "Medium"
    assigned_team = "General IT Support"

    if issue_type == "security_issue":
        priority = "High"
        assigned_team = "Security Operations"

    elif issue_type == "network_issue":
        priority = "Medium"
        assigned_team = "Network Team"

    elif issue_type == "hardware_issue":
        priority = "Medium"
        assigned_team = "Hardware Support"

    elif issue_type == "vpn_issue":
        priority = "Medium"
        assigned_team = "Remote Access Team"

    elif issue_type == "password_reset":
        priority = "Low"
        assigned_team = "Identity Management"

    if escalation_needed:
        priority = "High"

    return {
        "ticket_id": ticket_id,
        "priority": priority,
        "assigned_team": assigned_team,
        "status": "Open"
    }


def update_ticket_status(ticket, user_message):

    message = user_message.lower()

    confirmation_keywords = [
        "confirmed",
        "confirm",
        "issue is resolved",
        "fully resolved",
        "problem solved",
        "everything works now"
    ]

    resolved_keywords = [
        "fixed",
        "resolved",
        "working now",
        "issue resolved",
        "solved",
        "vpn works",
        "it works",
        "working again"
    ]

    escalation_keywords = [
        "still not working",
        "urgent",
        "affecting everyone",
        "critical",
        "outage",
        "cannot work",
        "business impact"
    ]

    # User confirms resolution
    if (
        ticket["status"] == "Awaiting Confirmation"
        and any(
            keyword in message
            for keyword in confirmation_keywords
        )
    ):

        ticket["status"] = "Resolved"

    # User indicates issue appears fixed
    elif any(
        keyword in message
        for keyword in resolved_keywords
    ):

        ticket["status"] = "Awaiting Confirmation"

    # Escalation trigger
    elif any(
        keyword in message
        for keyword in escalation_keywords
    ):

        ticket["status"] = "Escalated"

    # First follow-up interaction
    elif ticket["status"] == "Open":

        ticket["status"] = "In Progress"

    return ticket