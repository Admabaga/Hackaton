from typing import Optional
from pydantic import BaseModel

class DocumentResponseDTO(BaseModel):
    id: int
    action_id: int
    file_url: str
    summary: Optional[str]
    embedding: Optional[str]

    class Config:
        orm_mode = True