import scrapy
from scrapy.loader import ItemLoader
from Blockchain.items import BitkanItem

class BitkanSpider(scrapy.Spider):
    name = 'bitkan'
    allowed_domains = ['bitkan.com']

    def start_requests(self):
        url = 'http://www.bitkan.com/news/load_news'
        yield scrapy.FormRequest(
            url=url,
            formdata={"page": "20"},
            callback=self.parse,
        )

        def parse(self, response):
            print(response.status)
    # do something