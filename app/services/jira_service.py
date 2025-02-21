from datetime import datetime
from fastapi import HTTPException
from app.services.telex_service import send_telex_message
from app.core.config import settings

USER_NAME = settings.USER_NAME

# Allowed Jira events
ALLOWED_EVENTS = {"jira:issue_created", "jira:issue_updated"}

def format_created_at(timestamp: str):
    try:
        dt = datetime.strptime(timestamp[:19], "%Y-%m-%dT%H:%M:%S")
        return dt.strftime("%B %d, %Y at %I:%M %p UTC")
    except ValueError:
        return "Unknown"

def process_jira_event(event_data: dict):
    event_type = event_data.get("webhookEvent")

    if event_type not in ALLOWED_EVENTS:
        raise HTTPException(status_code=400, detail=f"Event {event_type} is not handled")

    issue = event_data.get("issue", {})
    fields = issue.get("fields", {})

    issue_key = issue.get("key", "Unknown")
    project_name = fields.get("project", {}).get("name", "Unknown")
    project_key = fields.get("project", {}).get("key", "Unknown")
    summary = fields.get("summary", "No summary provided")
    description = fields.get("description", "No description available")
    issue_type = fields.get("issuetype", {}).get("name", "Unknown")
    priority = fields.get("priority", {}).get("name", "Unknown")
    status = fields.get("status", {}).get("name", "Unknown")
    reporter = fields.get("reporter", {}).get("displayName", "Unknown")
    assignee = fields.get("assignee", {}).get("displayName", "Unassigned")
    created_at = format_created_at(fields.get("created", "Unknown"))
    issue_url = issue.get("self", "#")

    # Map issue type to emoji
    issue_type_emoji = {
        "Bug": "🐛",
        "Task": "✅",
        "Story": "📖",
        "Epic": "🗂️"
    }.get(issue_type, "📌")

    # Map priority to emoji
    priority_emoji = {
        "High": "🔥",
        "Medium": "⚡",
        "Low": "🟢"
    }.get(priority, "🔹")

    # Determine event-specific message
    event_name = "New Issue Created in Jira" if event_type == "jira:issue_created" else "Issue Updated in Jira"

    message = (
        f"🏗️ Project:{project_name} ({project_key})\n"
        f"🔑 Issue Key:{issue_key}\n"
        f"📌 Summary:{summary}\n"
        f"📝 Description:{description}\n"
        f"{issue_type_emoji} Type:{issue_type}\n"
        f"⚡ Priority:{priority_emoji} {priority}\n"
        f"📊 Status:{status}\n"
        f"🧑‍💻 Reporter:{reporter}\n"
        f"👤 Assignee:{assignee}\n"
        f"🕒 Created At:{created_at}\n"
        f"🔍 View Issue in Jira 🔗 {issue_url} "
    )


    send_telex_message(event_name, USER_NAME, "success", message)

    return {"processed": True, "message": message}
