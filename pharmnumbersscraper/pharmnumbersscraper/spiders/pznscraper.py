import scrapy
import pandas as pd
import openpyxl
import fsspec

from urllib.parse import quote
from scrapy.http import FormRequest

# our first spider
class PznscraperSpider(scrapy.Spider):
    name = "pznscraper"
    allowed_domains = ['dkv.com']

    def start_requests(self):
        # Load Excel data
        excel_path = r'C:\Users\jinji\Desktop\Data Science\Programming Projects\webscrapy\data files\testdata_pzn.xlsx'
        df = pd.read_excel(excel_path)

        # Iterate through PZN column and generate requests
        for pzn_number in df['PZN']:
            url = f'https://www.dkv.com/gesundheit-arzneimittel-preis-vergleich.html?start=1&init=1&cat=pzn&q={pzn_number}#preisvergleich'
            yield scrapy.Request(url, callback=self.parse, meta={'pzn_number': pzn_number})
            



    def parse(self, response):
        
        # Extract the price using the provided CSS selector
        price = response.css('div#arzneidetails table.comparemed tr td.price').get()

        # Extract PZN number from meta
        pzn_number = response.meta['pzn_number']

        # Update the Excel sheet with the price information
        self.update_excel(pzn_number, price)

    def update_excel(self, pzn_number, price):
        # Load Excel data
        excel_path = r'C:\Users\jinji\Desktop\Data Science\Programming Projects\webscrapy\data files\testdata_pzn.xlsx'
        df = pd.read_excel(excel_path)

        # Update the second column with the price
        df.loc[df['PZN'] == pzn_number, 'Price'] = price

        # Save the updated DataFrame to Excel
        df.to_excel(excel_path, index=False)


   
