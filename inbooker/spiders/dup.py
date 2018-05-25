# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector

class HnItem(scrapy.Item):
    country = scrapy.Field()
    name = scrapy.Field()
    type = scrapy.Field()

class PublisherSpider(scrapy.Spider):
    name = 'dup'
    allowed_domains = ['inbooker.com/pubs/publishers']
    start_urls = ['http://www.inbooker.com/pubs-{}/publishers'.format(i) for i in range(1,372)]

    def parse(self, response):
        sel = Selector(response)
        item = HnItem()
        country_list = sel.xpath("//tr/td[1]/span/text()").extract()
        name_list = sel.xpath("//tr/td[3]/a/text()").extract()
        type_list = sel.xpath("//tr/td[4]/text()").extract()
        for x in range(0,len(country_list)):
            item['country'] = country_list[x]
            item['name'] = name_list[x]
            item['type'] = type_list[x]
            yield item