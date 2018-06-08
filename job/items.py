# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JobItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    position_name = scrapy.Field()
    position_link = scrapy.Field()
    company_name = scrapy.Field()
    work_location = scrapy.Field()
    postiton_pay = scrapy.Field()
    publish_times = scrapy.Field()


class DescItem(scrapy.Item):
    position_duty = scrapy.Field()
    position_demand = scrapy.Field()
