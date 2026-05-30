import os


def load_knowledge(issue_type):

    knowledge_files = {
        "vpn_issue": "knowledge_base/vpn_guide.txt",
        "password_reset": "knowledge_base/password_reset.txt",
        "email_issue": "knowledge_base/outlook_guide.txt",
        "printer_issue": "knowledge_base/printer_support.txt",
        "m365_issue": "knowledge_base/m365_support.txt",
        "active_directory_issue": "knowledge_base/active_directory.txt",
        "general": "knowledge_base/general_support.txt"
    }

    file_path = knowledge_files.get(
        issue_type,
        "knowledge_base/general_support.txt"
    )

    if not os.path.exists(file_path):
        return ""

    with open(
        file_path,
        "r",
        encoding="utf-8"
    ) as file:

        return file.read()