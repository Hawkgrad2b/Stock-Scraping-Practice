#print('hello world')
from bs4 import BeautifulSoup
import requests

import csv
from datetime import datetime

SCRAPERAPI_URL = 'http://api.scraperapi.com'
SCRAPERAPI_KEY = '83fa2fd89b26ee07095793f138511cf0'

def get_page_results(stock_symbol):
    url = f'https://www.marketwatch.com/investing/stock/{stock_symbol}?mod=search_symbol'
    params = {
        'api_key' : SCRAPERAPI_KEY,
        'url' : url
    }
    response = requests.get(SCRAPERAPI_URL, params=params)
    return response.content
