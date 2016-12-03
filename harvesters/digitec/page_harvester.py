import requests
from bs4 import BeautifulSoup
import datetime


def request_page(url_extension):
    headers = {"user-agent": "Mozilla/5.0"}
    r = requests.get("https://www.digitec.ch" + url_extension, headers=headers).text
    return BeautifulSoup(r, "lxml")


def get_product_url_advent_calendar():
    soup = request_page("/de/LiveShopping/AdventCalendar")
    overlay_elements = soup.find(id="03").find_all("a", class_="overlay")
    return overlay_elements[0].get("href")


def get_product_url():
    soup = request_page("/de/LiveShopping")
    overlay_elements = soup.find_all("a", class_="overlay")
    return overlay_elements[0].get("href")


def harvest_page():
    current_date = datetime.datetime.now()
    if current_date.month == 12 and current_date.day < 25:
        product_url = get_product_url_advent_calendar()
    else:
        product_url = get_product_url()
    print(product_url)
