# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PagelvceliItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    station_name = scrapy.Field()
    time = scrapy.Field()
    air_temperature = scrapy.Field()
    air_temperature_trend = scrapy.Field()
    air_humidity = scrapy.Field()
    dew_point = scrapy.Field()
    precipitation = scrapy.Field()
    intensity = scrapy.Field()
    visibility = scrapy.Field()
    road_temperature1 = scrapy.Field()
    road_temperature1_trend = scrapy.Field()
    road_condition1 = scrapy.Field()
    road_warning1 = scrapy.Field()
    freezing_point1 = scrapy.Field()
    road_temperature2 = scrapy.Field()
    road_temperature2_trend = scrapy.Field()
    road_condition2 = scrapy.Field()
    road_warning2 = scrapy.Field()
    freezing_point2 = scrapy.Field()


#def keys(self):
        # in your preferred order
        #return ['station_name', 'time','air_temperature','air_temperature_trend','air_humidity','dew_point',
        #'precipitation','intensity','visibility', 'road_temperature1', 'road_temperature1_trend',
        #'road_condition1','road_warning1', 'freezing_point1', 'road_temperature2', 'road_temperature2_trend',
        #'road_condition2', 'road_warning2', 'freezing_point2']
