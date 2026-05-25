import random

def generate_ticket(issue_type, escalation_needed):

    ticket_id = f"INC-{random.randint(1000, 9999)}"

    # Default values
    priority = "Medium"
    assigned_team = "General IT Support"

    # Security issues
    if issue_type == "security_issue":
        priority = "High"
        assigned_team = "Security Operations"

    # Network issues
    elif issue_type == "network_issue":
        priority = "Medium"
        assigned_team = "Network Team"

    # Hardware issues
    elif issue_type == "hardware_issue":
        priority = "Medium"
        assigned_team = "Hardware Support"

    # VPN issues
    elif issue_type == "vpn_issue":
        priority = "Medium"
        assigned_team = "Remote Access Team"

    # Password issues
    elif issue_type == "password_reset":
        priority = "Low"
        assigned_team = "Identity Management"

    # Escalated issues become high priority
    if escalation_needed:
        priority = "High"

    return {
        "ticket_id": ticket_id,
        "priority": priority,
        "assigned_team": assigned_team,
        "status": "Open"
    }