# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from Blockchain.items import BitkanItem

class BitkanSpider(scrapy.Spider):
    name = 'bitkan'
    allowed_domains = ['bitkan.com']

    def start_requests(self):
        url = 'http://www.bitkan.com/news/load_news'
        for page in range(10,20,10):
            yield scrapy.FormRequest(
                url=url,
                formdata={"page": str(page)},
                callback=self.parse,
            )

    def parse(self, response):
        url_list = response.xpath('//h4[@class="news-title"]/a/@href').extract()
        for url in url_list:
            yield scrapy.Request(url,callback=self.parse_detail)


    def parse_detail(self,response):

        I = ItemLoader(item=BitkanItem(),response=response)
        I.add_xpath('title','//div[@class="news-v3-in"]/h2/text()')
        I.add_xpath('publish_time','//div[@class="news-v3-in"]/ul/li[2]/text()')
        I.add_xpath('content','//div[@class="news-v3-in"]/div/p/text() | //div[@class="news-v3-in"]/div/p/span/text()')
        I.add_value('url',response.url)

        yield I.load_item()


