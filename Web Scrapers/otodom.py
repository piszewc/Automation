# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 22:16:55 2019

@author: piotr
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd 

url = "https://www.otodom.pl/sprzedaz/mieszkanie/krakow/?search%5Bdist%5D=0&search%5Bsubregion_id%5D=410&search%5Bcity_id%5D=38"


def create_soup(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    pages = soup.find("div", class_="col-md-content section-listing__row-content")
    return pages

def load_max_page(url):
    soup = create_soup(url)
    page = soup.find("li", class_= "pager-counter")
    page = soup.find("strong", class_="current").find(text=True).strip()
    return(page)


def read_page(url):
    soup = create_soup(url)
    all_article = soup.find_all("article")
    print(all_article)




max_page = load_max_page(url)
read_page(url)

