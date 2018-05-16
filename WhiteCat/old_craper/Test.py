import requests
from bs4 import BeautifulSoup
from time import sleep
from multiprocessing import Pool

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}
html = None
links = None

r = requests.get('https://www.otodom.pl/sprzedaz/mieszkanie/krakow/?search%5Bdist%5D=0&search%5Bsubregion_id%5D=410&search%5Bcity_id%5D=38', headers=headers, timeout=10)

if r.status_code == 200:
    html = r.text
    soup = BeautifulSoup(html, 'lxml')
    listing_section = soup.select('#offer-item ad_id3l0ce')
    links = [link['href'].strip() for link in listing_section]
    print(listing_section)

# parse a single item to get information
