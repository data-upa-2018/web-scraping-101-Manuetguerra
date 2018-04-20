import scrapy

class QuotesSpider(scrapy.Spider):
    name = "cotizacion"
    def start_requests(self):
        urls = [
            'https://www.bcp.gov.py/webapps/web/cotizacion/monedas-mensual'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)


    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').extract_first(),
                'author': quote.xpath('span/small/text()').extract_first(),
            }

        next_page = response.css('li.next a::attr("href")').extract_first()
        if next_page is not None:
            yield response.follow(next_page, self.parse)




