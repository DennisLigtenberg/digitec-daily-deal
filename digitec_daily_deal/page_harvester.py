import requests
from bs4 import BeautifulSoup


def harvest_page():
    headers = {'user-agent': 'Mozilla/5.0'}
    r = requests.get('https://www.digitec.ch/de/LiveShopping', headers=headers).text
    soup = BeautifulSoup(r, 'lxml')
    overlay_elements = soup.find_all("a", class_="overlay")
    deal_path = overlay_elements[0].get('href')
    print(deal_path)
