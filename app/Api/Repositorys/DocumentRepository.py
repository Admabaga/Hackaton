from sqlalchemy.orm import Session
from app.Api.Models.Document import Document

class DocumentRepository:
    @staticmethod
    def createDocument(database: Session, document: Document):
        try:
            database.add(document)
            database.commit()
            database.refresh(document)
            return document
        except Exception as e:
            database.rollback()
            raise e

    @staticmethod
    def getDocumentsByAction(database: Session, actionId: int):
        return database.query(Document).filter_by(action_id=actionId).all()