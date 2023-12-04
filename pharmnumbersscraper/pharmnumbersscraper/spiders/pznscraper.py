import scrapy

#our first spider
class PznscraperSpider(scrapy.Spider):
    name = "pznscraper"
    allowed_domains = ["www.dkv.com"]
    start_urls = ["http://www.dkv.com/"]

    #will contain all the data we want to scrape
    def parse(self, response):
        pass
