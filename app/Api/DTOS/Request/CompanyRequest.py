from pydantic import BaseModel

class CompanyRequest(BaseModel):
    name: str
    nit: str