# Web Scraping Project


## Project Overview
Webscraper to scrape prices of medications (via their PZN code) from dkv.com. 

## Getting Started

**Prerequisites:**

Python (version 3.11.7)

Scrapy (install using `pip install scrapy`)

Pandas (install using `pip install pandas`)
# 


**Installation:**

Clone the repository: git clone https://github.com/HiAmara/webscraper-for-teamprojekt.git

In case you want to scrape different PZNs than specified in the 'example' excel file, adjust the excel path variable inside the spider pznscraper.py
Make sure there is a column named 'PZN'.

Open Terminal and Navigate to the project directory and then to the subfolder pharmnumbersscraper (`cd pharmnumbersscraper`)

Execute the spider with the following command: `scrapy crawl pznscraper`

After scraping you can use the formulas in the html_remover excel file to clean the scraped strings. 
#


**Spider Configuration**

It's possible to scrape items other than price if you find suitable css selectors.

You can try out selectors using the scrapy shell.
#

**Data Format**

The pzn numbers are inside an .xlsx file (scraper uses the file called "example") and the prices will be added to that same file.

The format is not ideal, i used excel formulas to fix this after the scrape --> see the excel sheet "html_remover" in data folder
#


**Contact**

uyvep@student.kit.edu

