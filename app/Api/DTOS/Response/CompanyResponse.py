from pydantic import BaseModel

class CompanyResponseDTO(BaseModel):
    id: int
    name: str
    nit: str
    class Config:
        orm_mode = True