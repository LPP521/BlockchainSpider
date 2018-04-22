# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
import datetime
import re

from  Blockchain.settings import SQL_DATETIME_FORMAT
import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, MapCompose, Join
from w3lib.html import remove_tags


class BlockchainItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class EightbtcItem(scrapy.Item):
    url = scrapy.Field(output_processor=TakeFirst(),)
    title = scrapy.Field(output_processor=TakeFirst(),)
    publish_time = scrapy.Field(output_processor=TakeFirst(),)
    content = scrapy.Field(output_processor=Join('<br>'))

    def get_insert_sql(self):
        # 插入表的sql语句
        insert_sql = """
            insert into eightbtc(url,title, publish_time, content) VALUES (%s, %s, %s, %s)
        """
        params = (
            self["url"],
            self["title"],
            self["publish_time"],
            self["content"],
        )

        return insert_sql, params

class JinseItem(scrapy.Item):
    url = scrapy.Field(output_processor=TakeFirst(),)
    title = scrapy.Field(output_processor=TakeFirst(),)
    publish_time = scrapy.Field(output_processor=TakeFirst(),)
    content = scrapy.Field(output_processor=Join('<br>'))

    def get_insert_sql(self):
        # 插入表的sql语句
        insert_sql = """
           insert into jinse(url , title, publish_time,content) VALUES (%s, %s, %s,%s )
        """
        params = (
            self["url"],
            self["title"],
            self["publish_time"],
            self["content"],
        )

        return insert_sql, params

class BitkanItem(scrapy.Item):
    url = scrapy.Field(output_processor=TakeFirst(),)
    title = scrapy.Field(output_processor=TakeFirst(),)
    publish_time = scrapy.Field(output_processor=TakeFirst(),)
    content = scrapy.Field(output_processor=Join('<br>'))

    def get_insert_sql(self):
        # 插入表的sql语句
        insert_sql = """
           insert into bitkan(url , title, publish_time,content) VALUES (%s, %s, %s,%s )
        """
        params = (
            self["url"],
            self["title"],
            self["publish_time"],
            self["content"],
        )

        return insert_sql, params
