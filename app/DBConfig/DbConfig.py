from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import Engine
from sqlalchemy.ext.declarative import declarative_base


connectionToDataBase="mysql+mysqlconnector://root:""@localhost:3306/hackatondb"

engine = create_engine(connectionToDataBase)

sessionLocal = sessionmaker(autocommit = False, autoflush = False, bind = engine)

Base = declarative_base()
def getDataBase():
    basedatos = sessionLocal()
    try:
        yield basedatos
    except Exception as error:
        basedatos.rollback()
        raise error
    finally:
        basedatos.close()