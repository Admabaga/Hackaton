from pydantic import BaseModel

class DocumentRequest(BaseModel):
    file_url: str
    summary: str
    embedding: str