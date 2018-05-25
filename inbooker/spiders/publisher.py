# -*- coding: utf-8 -*-
import scrapy


class PublisherSpider(scrapy.Spider):
    name = 'publisher'
    allowed_domains = ['inbooker.com/pubs/publishers']
    start_urls = ['http://www.inbooker.com/pubs-{}/publishers'.format(i) for i in range(1,4)]

    def parse(self, response):
        country = response.xpath("//tr/td[1]/span/text()").extract()
        name = response.xpath("//tr/td[3]/a/text()").extract()
        type = response.xpath("//tr/td[4]/text()").extract()

        yield {
            'Name': name,
            'Country': country,
            'Type': type
        }

