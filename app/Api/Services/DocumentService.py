from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.Api.DTOS.Request.DocumentRequest import DocumentRequest
from app.Api.Models.Action import Action
from app.Api.Models.Document import Document
from app.Api.Repositorys.DocumentRepository import DocumentRepository

class DocumentService:
    def createDocument(self, database: Session, dto: DocumentRequest, actionId : int):
        self.validateAction(actionId, database)
        document = Document(**dto.dict())
        document.action_id = actionId
        return DocumentRepository.createDocument(database, document)

    def getDocumentsByAction(self, database: Session, actionId: int):
        documents = DocumentRepository.getDocumentsByAction(database, actionId)
        if not documents:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"No hay documentos relacionados a la accion."
            )
        return documents

    def validateAction(self, actionId: int, database: Session):
        action = database.query(Action).filter(Action.id == actionId).first()
        if not action:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Accion no encontrada.")