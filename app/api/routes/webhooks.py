from fastapi import APIRouter, HTTPException, Request
from http import HTTPStatus
from app.services.jira_service import process_jira_event

router = APIRouter()

@router.post("/",
    status_code=HTTPStatus.CREATED, 
    summary="Receive JIRA webhook", 
    description="Receives and processes JIRA webhook events",
    responses={
        HTTPStatus.CREATED: {
            "description": "Event received successfully",
            "content": {
                "application/json": {
                    "example": {
                        "message": "Event received",
                        "details": {"key": "value"}
                    }
                }
            }
        },
        HTTPStatus.BAD_REQUEST: {
            "description": "Invalid payload",
            "content": {
                "application/json": {
                    "example": {"detail": "Invalid payload"}
                }
            }
        }
    })
async def jira_webhook(request: Request):
    """Handles incoming JIRA webhooks and processes the event."""
    event_data = await request.json()
    
    if not event_data:
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST, detail="Invalid payload")

    response = process_jira_event(event_data)
    
    return {"message": "Event received", "details": response}

