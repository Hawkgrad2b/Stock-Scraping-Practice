#print('hello world')
from bs4 import BeautifulSoup
import requests

import csv
from datetime import datetime

SCRAPERAPI_URL = 'http://api.scraperapi.com'
SCRAPERAPI_KEY = '83fa2fd89b26ee07095793f138511cf0'

stock_symbols = ['aapl', 'ssnlf', 'tsla']
 
csv_headers = [
    'Date', 'Symbol', 'Price', 'Open', 'Day Range', '52 Week Range', 'Market Cap',
    'Shares Outstanding', 'Public Float', 'Beta', 'Rev. per Employee', 'P/E Ratio',
    'EPS', 'Yield', 'Dividend', 'Ex-Dividend Date', 'Short Interest', '% of Float Shorted',
    'Average Volume'
]


def get_page_results(stock_symbol):
    url = f'https://www.marketwatch.com/investing/stock/{stock_symbol}?mod=search_symbol'
    params = {
        'api_key' : SCRAPERAPI_KEY,
        'url' : url
    }
    response = requests.get(SCRAPERAPI_URL, params=params)
    return response.content

def extract_data(page_content):
    soup = BeautifulSoup(page_content, 'html.parser')

    main_price = soup.find('bg-quote', attrs={'class':'value'}).text

    additional_data = {}
    for item in soup.findAll('li', attrs={'class':'kv__item'}):
        label = item.find('small', attrs={'class':'label'}).text
        value = item.find('span', attrs={'class':'primary'}).text
        additional_data[label] = value
    return main_price, additional_data


