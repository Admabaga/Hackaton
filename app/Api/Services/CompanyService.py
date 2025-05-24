from sqlalchemy.orm import Session
from app.Api.DTOS.Request.CompanyRequest import CompanyRequest
from app.Api.Models.Company import Company
from app.Api.Repositorys.CompanyRepository import CompanyRepository

class CompanyService:

    def createCompany(self, database: Session, dto: CompanyRequest):
        company = Company(**dto.dict())
        return CompanyRepository.createCompany(database, company)

    def getAllCompanies(self, database: Session):
        return CompanyRepository.getAllCompanies(database)