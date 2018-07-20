import scrapy
from scrapy.loader import ItemLoader
from tutorial.items import Quote

class QuotesSpider(scrapy.Spider):
    name = "quotes2"

    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for quote in response.css('div.quote'):
            l = ItemLoader(Quote(), quote)
            l.add_css('text', 'span.text::text')
            l.add_css('author', 'small.author::text')
            l.add_css('tags', 'div.tags a.tag::text')
            yield l.load_item()
