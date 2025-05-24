from sqlalchemy.orm import Session
from app.Api.Models.Company import Company

class CompanyRepository:
    @staticmethod
    def createCompany(database: Session, company: Company):
        try:
            database.add(company)
            database.commit()
            database.refresh(company)
            return company
        except Exception as e:
            database.rollback()
            raise e

    @staticmethod
    def getAllCompanies(database: Session):
        return database.query(Company).all()