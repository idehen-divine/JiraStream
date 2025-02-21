import httpx
from app.core.config import settings

TELEX_WEBHOOK_URL = settings.TELEX_WEBHOOK_URL

def send_telex_message(event_name: str, username: str, status: str, message: str):
    if not TELEX_WEBHOOK_URL:
        raise ValueError("Telex webhook URL not configured")

    payload = {
        "event_name": event_name,
        "username": username,
        "status": status,
        "message": message
    }

    response = httpx.post(TELEX_WEBHOOK_URL, json=payload)

    if response.status_code not in [200, 201, 202]:
        raise Exception(f"Failed to send message to Telex: {response.text}")
    
    return response.json()
