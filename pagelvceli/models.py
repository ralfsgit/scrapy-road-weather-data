from sqlalchemy import create_engine, Column, Table, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (
    Integer, SmallInteger, String, Date, DateTime, Float, Boolean, Text, LargeBinary)

from scrapy.utils.project import get_project_settings

DeclarativeBase = declarative_base()

def db_connect():
    """
    Performs database connection using database settings from settings.py.
    Returns sqlalchemy engine instance
    """
    return create_engine(get_project_settings().get("CONNECTION_STRING"))

def create_table(engine):
    DeclarativeBase.metadata.create_all(engine)

class RoadWeatherDB(DeclarativeBase):
    __tablename__ = "road_table"

    id = Column(Integer, primary_key=True)
    precipitation = Column('precipitation', String(40))
    air_temperature_trend = Column('air_temperature_trend', String(40))
    dew_point = Column('dew_point', Float())
    freezing_point2 = Column('freezing_point2', Float())
    road_warning1 = Column('road_warning1', String(40))
    road_warning2 = Column('road_warning2', String(40))
    freezing_point1 = Column('freezing_point1', Float())
    intensity = Column('intensity', Float())
    visibility = Column('visibility', Float())
    road_temperature1_trend = Column('road_temperature1_trend', Float())
    road_temperature2_trend = Column('road_temperature2_trend', Float())
    air_temperature = Column('air_temperature', Float())
    time = Column('time', String(40))
    road_condition2 = Column('road_condition2', String(40))
    air_humidity = Column('air_humidity', Float())
    station_name = Column('station_name', String(100))
    road_temperature2 = Column('road_temperature2', Float())
    road_condition1 = Column('road_condition1', String(40))
    road_temperature1 = Column('road_temperature1', Float())
