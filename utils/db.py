from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, Float, DateTime
import pymysql
from utils.config import cfg


# MYSQL_DATABASE_URL = "mysql+pymysql://user:user@db:3306/demo"
# MYSQL_DATABASE_URL = "mysql+pymysql://user:user@localhost:3306/demo"
# MYSQL_DATABASE_URL = "mysql+pymysql://petamva:Pet%40mv%40134679-852@195.251.3.230:30002/petamva_demo22"
MYSQL_DATABASE_URL = cfg.db_url
engine = create_engine(MYSQL_DATABASE_URL)
SessionFactory = sessionmaker(bind=engine, autocommit=False, future=True, autoflush=False)
Base = declarative_base()


class Alerts(Base):
    __tablename__ = 'Alerts'  # this is mandatory

    id = Column(Integer, primary_key=True, index=True)  # at least one column with a primary key
    Timestamp = Column(DateTime)
    FarmKey = Column(Integer)
    SensorKey = Column(Integer)
    SensorValue = Column(Float)


# class Predictions(Base):
#     __tablename__ = 'Predictions' 

#     id = Column(Integer, primary_key=True, index=True)  
#     DiffuseSolarRadAvg = Column(Float)
#     SolarRadAvg = Column(Float)
#     WindSpeedAvg = Column(Float)
#     Temperature = Column(Float)
#     LeafInfraredAvg = Column(Float)
#     RelHumidityAvg = Column(Float)
#     LeafWetness = Column(Float)


Base.metadata.create_all(bind=engine)