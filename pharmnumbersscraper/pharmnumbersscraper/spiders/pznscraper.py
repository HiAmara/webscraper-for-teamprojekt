import scrapy
import pandas as pd
from pharmnumbersscraper.items import HealthProductItem
from urllib.parse import quote
from scrapy.http import FormRequest

# our first spider
class PznscraperSpider(scrapy.Spider):
    name = "pznscraper"
    allowed_domains = ["www.dkv.com"]
    start_urls = ["http://www.dkv.com/"]

    # will contain all the data we want to scrape
    def parse(self, response):
        excel_path = "C://Users//jinji//Desktop//Data Science//Programming Projects//webscrapy//data files//testdata_pzn.xlsx"
        df = pd.read_excel(excel_path)

        for index, row in df.iterrows():
            if pd.isna(row['PZN']):
                search_term = row['Arzneimittelbezeichnung']
                search_url = f"https://www.dkv.com/gesundheit-arzneimittel-preis-vergleich.html?start=1&init=1&cat=handelsname&q={quote(search_term)}#preisvergleich"

                # Follow the search URL to scrape results
                yield scrapy.Request(url=search_url, callback=self.parse_search_results, meta={'pzn': row['PZN'], 'search_term': search_term})

    def parse_search_results(self, response):
        first_result_button_xpath = '/html/body/div[2]/div[4]/div/div/div/div/div/div[1]/form/button'
        yield from response.follow_all(first_result_button_xpath, callback=self.parse_pzn)

    def parse_pzn(self, response):
    #    # Print the URL the spider is going to
        self.logger.info(f"Going to URL: {response.url}")

        # Extract the missing PZN from the new page
        pzn_xpath = '/html/body/div[2]/div[4]/div/div/div/div/div[2]/div[2]/div[1]/p[1]/strong/following-sibling::text()'
        pzn_value = response.xpath(pzn_xpath).get()

        # Return the PZN value
        yield {'pzn': pzn_value.strip() if pzn_value else None}
