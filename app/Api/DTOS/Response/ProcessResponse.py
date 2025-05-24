from pydantic import BaseModel
from datetime import datetime

class ProcessResponseDTO(BaseModel):
    id: int
    company_id: int
    code: str
    court: str
    updated_at: datetime
    class Config:
        orm_mode = True