# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from Blockchain.items import EightbtcItem
from scrapy_redis.spiders import RedisSpider

class EightbtcSpider(scrapy.Spider):
    name = 'eightbtc'
    allowed_domains = ['8btc.com']
    start_urls = ['http://www.8btc.com/sitemap?newPost=1&pg={}'.format(str(i) for i in range(1,2))]

    def parse(self, response):
        detail_urls = response.xpath('//a[@class="title"]/@href')
        for url in detail_urls:
            list_a = response.urljoin(url.extract())
            yield scrapy.Request(list_a,callback=self.detail_parse)

    def detail_parse(self,response):
        I = ItemLoader(item=EightbtcItem(), response=response)
        I.add_xpath('title','//div[@class="article-title"]/h1/text()')
        I.add_xpath('publish_time','//div[@class="single-crumbs clearfix"]/span/time/text()')
        I.add_xpath('content','//div[@class="article-content"]/p/text()'.strip())
        I.add_value('url',response.url)

        Eightbtc_item = I.load_item()
        yield Eightbtc_item