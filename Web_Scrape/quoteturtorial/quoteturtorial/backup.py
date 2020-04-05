import scrapy
from scrapy.http import FormRequest
from items import QuoteturtorialItem
class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    page_number = 2
    start_urls = [
        'http://quotes.toscrape.com/login'
        ]
    def parse(self,response):
        token = response.css('form input::attr(value)').extract_first()
        return FormRequest.from_response(response, formdata={
            'csrf_token': token,
            'username': 'Mozesthegreat@yahoo.com',
            'password': 'giberish'
        }, callback= self.start_scraping)

    def start_scraping(self,response):
        tems = QuoteturtorialItem()

        all_div_quotes = response.css('div.quote')

        for quote in all_div_quotes:
            title = quote.css('span.text::text').extract()
            author = quote.css('.author::text').extract()
            tag = quote.css('.tag::text').extract()

            items['title'] = title
            items['author'] = author
            items['tag'] = tag
            yield items
