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

Adjust the excel path variable inside the spider pznscraper.py

Navigate to the project directory and then to the subfolder pharmnumbersscraper (`cd pharmnumbersscraper`)

Execute the spider with the following command: `scrapy crawl your_spider`
#


**Spider Configuration**

It's possible to scrape items other than price if you find suitable css selectors.
#

**Data Format**

The pzn numbers are inside an .xlsx file and the prices will be added to that same file.
#


**Contact**

uyvep@student.kit.edu

