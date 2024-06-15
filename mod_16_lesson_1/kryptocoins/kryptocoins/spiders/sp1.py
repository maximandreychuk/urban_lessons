import scrapy


class Sp1Spider(scrapy.Spider):
    name = "sp1"
    allowed_domains = ["coinmarketcap.com"]
    start_urls = ["https://coinmarketcap.com/ru/"]

    def parse(self, response):
        # names = response.xpath(
        #     '//*[@class="sc-71024e3e-0 ehyBa-d"]/text()').extract()
        quotes = response.xpath(
            '//*[@class="sc-4c05d6ef-0 sc-1c5f2868-2 dlQYLv bszTYj  hide-ranking-number"]')

        # for quote in quotes:
        #     coin = quote.xpath(
        #         './/*[@class="sc-71024e3e-0 ehyBa-d"]/text()').extract_first()
        yield {'coin': quotes}
