from pydantic import BaseModel
from datetime import date

class ActionRequest(BaseModel):
    type: str
    date: date
    description: str
    urgency: str