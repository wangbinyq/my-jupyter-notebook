import scrapy

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'http://quotes.toscrape.com/tag/humor/'
    ]

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').extract_first(),
                'author': quote.xpath('span/small/text()').extract_first()
            }

        next_page = response.css('li.next a::attr("href")').extract_first()
        if next_page is not None:
            yield response.follow(next_page, self.parse)

'''
1. built-in support for HTML/XML manipulate with regular expressions support.
2. interactive shell console
3. built-in feed exports
4. robust encoding support and auto-detection
5. strong extensibility support
6. built-in extensions and middlewares
7. telnet console hook into scrapy process
'''