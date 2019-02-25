# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from sqlalchemy.orm import sessionmaker
from models import RoadWeatherDB, db_connect, create_table

class PagelvceliPipeline(object):
    def __init__(self):
        """
        Initializes database connection and sessionmaker.
        Creates deals table.
        """
        engine = db_connect()
        create_table(engine)
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        """Save deals in the database.

        This method is called for every item pipeline component.
        """
        session = self.Session()
        quotedb = RoadWeatherDB()
        quotedb.precipitation = item["precipitation"]
        quotedb.air_temperature_trend = item['air_temperature_trend']
        quotedb.dew_point =  item['dew_point']
        quotedb.freezing_point2 = item['freezing_point2']
        quotedb.road_warning1 =  item['road_warning1']
        quotedb.road_warning2 =  item['road_warning2']
        quotedb.freezing_point1 =  item['freezing_point1']
        quotedb.intensity =  item['intensity']
        quotedb.visibility =  item['visibility']
        quotedb.road_temperature1_trend = item['road_temperature1_trend']
        quotedb.road_temperature2_trend = item['road_temperature2_trend']
        quotedb.air_temperature = item['air_temperature']
        quotedb.time = item['time']
        quotedb.air_humidity = item['air_humidity']
        quotedb.station_name = item['station_name']
        quotedb.road_temperature2 = item['road_temperature2']
        quotedb.road_condition1 = item['road_condition1']
        quotedb.road_temperature1 = item['road_temperature1']

        try:
            session.add(quotedb)
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()

        return item