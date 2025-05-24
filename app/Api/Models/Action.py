from sqlalchemy import Column, Date, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship
from app.DBConfig.DbConfig import Base

class Action(Base):
    __tablename__ = "actions"
    id = Column(Integer, primary_key=True)
    process_id = Column(Integer, ForeignKey("processes.id"))
    type = Column(String(100))
    date = Column(Date)
    description = Column(Text)
    urgency = Column(String(50))
    process = relationship("Process", back_populates="actions")
    documents = relationship("Document", back_populates="action")