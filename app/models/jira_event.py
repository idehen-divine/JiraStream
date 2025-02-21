from pydantic import BaseModel
from typing import Dict, Any

class JiraEvent(BaseModel):
    webhookEvent: str
    issue: Dict[str, Any]
