# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
# from scrapy.spiders import CrawlSpider, Rule
from scrapy.spiders import  Rule
from scrapy_redis.spiders import RedisCrawlSpider
from scrapy.loader import ItemLoader
from Blockchain.items import EightbtcItem

# class EightbtcaSpider(CrawlSpider):
class EightbtcaSpider(RedisCrawlSpider):
    name = 'eightbtc'
    allowed_domains = ['8btc.com']
    # start_urls = ['http://www.8btc.com/sitemap?newPost=1&pg=1']
    redis_key = "eightspider:start_urls"
    rules = (
        # Rule(LinkExtractor(allow=r'.*8btc.com/sitemap?newPost=1&pg=\d+')),
        Rule(LinkExtractor(restrict_xpaths=('//span[@class="page_link"]/a'))),
        Rule(LinkExtractor(restrict_xpaths=('//li[@class="itm itm_new"]/a')), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        I = ItemLoader(item=EightbtcItem(), response=response)
        I.add_xpath('title', '//div[@class="article-title"]/h1/text()')
        I.add_xpath('publish_time', '//div[@class="single-crumbs clearfix"]/span/time/text()')
        I.add_xpath('content', '//div[@class="article-content"]/p/text()'.strip())
        I.add_value('url', response.url)

        Eightbtc_item = I.load_item()
        yield Eightbtc_item