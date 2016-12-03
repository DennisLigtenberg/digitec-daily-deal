from bs4 import BeautifulSoup as bs
from product import Product
import requests
import re
import json

class ProviderDaydeal:
    url = "https://www.daydeal.ch/"
    product = Product


    def __init__(self):
        self._fetch_latest_product()

    def get_latest_product(self):
        return self.product

    def _fetch_latest_product(self):
        try:
            r = requests.get(self.url).text
        except Exception:
            print("Error getting latest url")

        soup = bs(r, "lxml")
        js = soup.findAll("script", type="text/javascript")

        product_id = (re.search('(product_id: \'[0-9]{1,10}\',)', str(js))).group()
        product_name = (re.search('(product_name:.\'\D{0,1024}\',)', str(js))).group()
        product_price = (re.search('(product_price: \'[0-9]{0,5}\.[0-9]{0,5}\'),', str(js))).group()

        self.product.product_price = product_price