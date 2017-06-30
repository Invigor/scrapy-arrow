import scrapy


class ManufacturersSpider(scrapy.Spider):
    name = "manufacturers"

    def start_requests(self):
        urls = [
            'https://www.arrow.com/en/manufacturers',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)


    def parse(self, response):
        for manufacturer in response.css('.ManufacturersTabs-results-item'):
            yield {
                'url': manufacturer.xpath('@href').extract_first(),
                'name': manufacturer.css('.ManufacturersTabs-results-item-text::text').extract_first(),
            }
