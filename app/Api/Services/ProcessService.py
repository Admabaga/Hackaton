from sqlalchemy.orm import Session
from app.Api.DTOS.Request.ProcessRequest import ProcessRequest
from app.Api.Models.Company import Company
from app.Api.Models.Process import Process
from app.Api.Repositorys.ProcessRepository import ProcessRepository
from fastapi import HTTPException, status

class ProcessService:
    def createProcess(self, database: Session, dto: ProcessRequest, companyId : int ):
        self.validateCompany(companyId, database)
        process = Process(**dto.dict())
        process.company_id = companyId
        return ProcessRepository.createProcess(database, process)

    def getByCompany(self, database: Session, companyId: int):
        self.validateCompany(companyId, database)
        process = ProcessRepository.getByCompany(database, companyId)
        if not process:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"No hay procesos relacionadas a la compañia."
            )
        return process

    def validateCompany(self, companyId : int, database: Session):
        company = database.query(Company).filter(Company.id == companyId).first()
        if not company:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Compañia no encontrada.")