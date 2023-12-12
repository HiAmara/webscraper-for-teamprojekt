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

    #path to excel file which contains the pzn numbers
    excel_path = "C://Users//jinji//Desktop//Data Science//Programming Projects//webscrapy//data files//testdata_pzn.xlsx"
    df = pd.read_excel(excel_path)
    numbers = df['PZN'].tolist()



    def start_requests(self):
        # Iterate through numbers and create requests
        for number in self.numbers:
            yield scrapy.Request(url=f'https://www.dkv.com/gesundheit-arzneimittel-preis-vergleich.html?start=1&init=1&cat=pzn&q={quote(number)}#preisvergleich', callback=self.parse)


    def parse(self, response):
        # Extract the price using the provided CSS selector
        price = response.css('#arzneidetails > table.comparemed > tbody > tr:nth-child(1) > td.price::text').get()

        # Update the DataFrame with the extracted price
        number = response.meta['number']
        row_index = self.df[self.df['PZN'] == number].index[0]
        self.df.at[row_index, 'Price'] = price

        # Save the updated DataFrame back to the Excel file
        self.df.to_excel('path/to/your/excel/file_updated.xlsx', index=False)


    ##functions i need
    # puts pzn into search bar and clicks on search
    # css path or xpath to price
    # add price to excel file

