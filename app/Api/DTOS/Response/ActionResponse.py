from pydantic import BaseModel
from datetime import date

class ActionResponseDTO(BaseModel):
    id: int
    process_id: int
    type: str
    date: date
    description: str
    urgency: str
    class Config:
        orm_mode = True