
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.Api.DTOS.Request.ActionRequest import ActionRequest
from app.Api.Models.Action import Action
from app.Api.Models.Process import Process
from app.Api.Repositorys.ActionRepository import ActionRepository

class ActionService:
    def createAction(self, database: Session, dto: ActionRequest, processId: int):
        self.validateProcess(processId, database)
        action = Action(**dto.dict())
        action.process_id = processId
        return ActionRepository.createAction(database, action)

    def getActionsByProcess(self, database: Session, processId: int):
        self.validateProcess(processId, database)
        actions = ActionRepository.getActionsByProcess(database, processId)
        if not actions:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"No hay acciones relacionadas al proceso."
            )
        return actions

    def validateProcess(self, processId : int, database: Session):
        process = database.query(Process).filter(Process.id == processId).first()
        if not process:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Proceso no encontrado.")