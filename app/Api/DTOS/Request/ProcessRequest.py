from pydantic import BaseModel
from datetime import datetime

class ProcessRequest(BaseModel):
    code: str
    court: str
    updated_at: datetime