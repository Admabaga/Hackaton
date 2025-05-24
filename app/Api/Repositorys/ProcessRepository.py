from sqlalchemy.orm import Session
from app.Api.Models.Process import Process

class ProcessRepository:
    @staticmethod
    def createProcess(database: Session, process: Process):
        try:
            database.add(process)
            database.commit()
            database.refresh(process)
            return process
        except Exception as e:
            database.rollback()
            raise e

    @staticmethod
    def getByCompany(database: Session, companyId):
        return database.query(Process).filter_by(company_id=companyId).all()