from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship
from app.DBConfig.DbConfig import Base

class Document(Base):
    __tablename__ = "documents"
    id = Column(Integer, primary_key=True)
    action_id = Column(Integer, ForeignKey("actions.id"))
    file_url = Column(String(255))
    summary = Column(Text)
    embedding = Column(Text)
    action = relationship("Action", back_populates="documents")