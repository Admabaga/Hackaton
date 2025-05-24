from sqlalchemy.orm import Session
from app.Api.Models.Action import Action

class ActionRepository:
    @staticmethod
    def createAction(database: Session, action: Action):
        try:
            database.add(action)
            database.commit()
            database.refresh(action)
            return action
        except Exception as e:
            database.rollback()
            raise e

    @staticmethod
    def getActionsByProcess(database: Session, processId: int ):
       return database.query(Action).filter_by(process_id=processId).all()