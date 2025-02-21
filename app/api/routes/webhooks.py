from fastapi import APIRouter, Request

router = APIRouter()

@router.post("/")
async def jira_webhook(request: Request):
    """Handles incoming JIRA webhooks and processes the event."""
    

