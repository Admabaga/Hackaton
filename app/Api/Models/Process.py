from sqlalchemy import Column,DateTime, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.DBConfig.DbConfig import Base

class Process(Base):
    __tablename__ = "processes"
    id = Column(Integer, primary_key=True)
    company_id = Column(Integer, ForeignKey("companies.id"))
    code = Column(String(100))
    court = Column(String(255))
    updated_at = Column(DateTime)
    company = relationship("Company", back_populates="processes")
    actions = relationship("Action", back_populates="process")

