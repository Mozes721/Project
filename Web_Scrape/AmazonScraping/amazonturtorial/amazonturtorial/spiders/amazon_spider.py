# -*- coding: utf-8 -*-
import scrapy

from ..items import AmazonturtorialItem


class AmazonSpiderSpider(scrapy.Spider):
    name = 'amazon_spider'
    start_urls = ['https://www.amazon.de/b/?node=419914031&ref_=Oct_CateC_117_0&pf_rd_p=03d09e17-5978-54d9-b579-984eacfd3fd0&pf_rd_s=merchandised-search-4&pf_rd_t=101&pf_rd_i=117&pf_rd_m=A3JWKAKR8XB7XF&pf_rd_r=CQCZWHXGXYS1G37F77JH&pf_rd_r=CQCZWHXGXYS1G37F77JH&pf_rd_p=03d09e17-5978-54d9-b579-984eacfd3fd0',
                  ]

    def parse(self, response):
        items = AmazonturtorialItem()

        product_name = response.css('.s-access-title::text').extract()
        product_author = response.css('.a-color-secondary .a-text-normal').css('::text').extract()
        product_price = response.css('.a-color-secondary+ .a-text-bold').css('::text').extract()
        product_imglink = response.css('.cfMarker::attr(src)').extract()

        items['product_name'] = product_name
        items['product_author'] = product_author
        items['product_price'] = product_price
        items['product_imglink'] = product_imglink

        yield items

