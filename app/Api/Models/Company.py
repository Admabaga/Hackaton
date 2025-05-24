from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.DBConfig.DbConfig import Base

class Company(Base):
    __tablename__ = "companies"
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    nit = Column(String(100))
    processes = relationship("Process", back_populates="company")
