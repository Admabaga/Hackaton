from typing import List

from fastapi.params import Depends
from fastapi import APIRouter
from sqlalchemy.orm import Session

from app.Api.DTOS.Response.ActionResponse import ActionResponseDTO
from app.Api.DTOS.Response.CompanyResponse import CompanyResponseDTO
from app.Api.DTOS.Response.DocumentResponse import DocumentResponseDTO
from app.Api.DTOS.Response.ProcessResponse import ProcessResponseDTO
from app.DBConfig.DbConfig import getDataBase
from app.Api.DTOS.Request.ActionRequest import ActionRequest
from app.Api.DTOS.Request.CompanyRequest import CompanyRequest
from app.Api.DTOS.Request.DocumentRequest import DocumentRequest
from app.Api.DTOS.Request.ProcessRequest import ProcessRequest
from app.Api.Services.CompanyService import CompanyService
from app.Api.Services.ProcessService import ProcessService
from app.Api.Services.ActionService import ActionService
from app.Api.Services.DocumentService import DocumentService

routes = APIRouter()

@routes.post("/companies", response_model= CompanyResponseDTO)
def createCompany(dto: CompanyRequest, database: Session = Depends(getDataBase)):
    return CompanyService().createCompany(database, dto)

@routes.get("/companies", response_model= List[CompanyResponseDTO])
def getCompanies(database: Session = Depends(getDataBase)):
    return CompanyService().getAllCompanies(database)

@routes.post("/processes/{companyId}", response_model= ProcessResponseDTO)
def createProcess(companyId: int, dto: ProcessRequest, database: Session = Depends(getDataBase)):
    return ProcessService().createProcess(database, dto, companyId)

@routes.get("/companies/{companyId}/processes", response_model= List[ProcessResponseDTO])
def getProcessesByCompany(companyId: int, database: Session = Depends(getDataBase)):
    return ProcessService().getByCompany(database, companyId)

@routes.post("/actions/{processId}", response_model= ActionResponseDTO)
def createAction(processId: int, dto: ActionRequest, database: Session = Depends(getDataBase)):
    return ActionService().createAction(database, dto, processId)

@routes.get("/processes/{processId}/actions", response_model= List[ActionResponseDTO])
def getActionsByProcess(processId: int, database: Session = Depends(getDataBase)):
    return ActionService().getActionsByProcess(database, processId)

@routes.post("/documents/{actionId}", response_model= DocumentResponseDTO)
def createDocument(actionId: int, dto: DocumentRequest, database: Session = Depends(getDataBase)):
    return DocumentService().createDocument(database, dto, actionId)

@routes.get("/actions/{actionId}/documents", response_model= List[DocumentResponseDTO])
def getDocumentsByAction(actionId: int, database: Session = Depends(getDataBase)):
    return DocumentService().getDocumentsByAction(database, actionId)