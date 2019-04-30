# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 22:16:55 2019

@author: piotr
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd 



def create_soup(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    pages = soup.find("div", class_="col-md-content section-listing__row-content")
    return pages

def load_max_page(url):
    soup = create_soup(url)
    page = soup.find("li", class_= "pager-counter")
    page = soup.find("strong", class_="current").find(text=True).strip()
    return page


def read_page(url):
    soup = create_soup(url)
    all_article = soup.find_all("article")
    
    article_list = []
    
    for article in all_article:
        title = article.find('span', class_="offer-item-title").find(text=True).strip()
        location = article.find('p').find(text=True).strip()
        item_id = article['data-tracking-id']
        item_url = article['data-url']
        item_type = article['data-featured-name']
        price = article.find('li', class_="offer-item-price").find(text=True).strip()
        rooms = article.find('li', class_="offer-item-rooms hidden-xs").find(text=True).strip()
        m2 = article.find('li', class_="hidden-xs offer-item-area").find(text=True).strip()
        article_list.append([item_type,item_id,item_url,title,location,price,rooms,m2])
        
    return article_list

def create_link(url,current_page):   
    link = str(url+str(current_page))
    return link


home_database = pd.DataFrame(columns=['item_type','id','url','title','location','price','rooms','m2'])

current_page = 1     

url = "https://www.otodom.pl/sprzedaz/mieszkanie/krakow/?search%5Bdist%5D=0&search%5Bsubregion_id%5D=410&search%5Bcity_id%5D=38&nrAdsPerPage=72&page="+str(current_page)
max_page = load_max_page(url)

print("Max Page is:", max_page)

while current_page <= max_page:
    print("Current Page:",current_page)
    current_link = create_link(url,current_page)
    
    page_items = read_page(current_link)
    load_home_database = pd.DataFrame(page_items,columns=['item_type','id','url','title','location','price','rooms','m2'])
    home_database = home_database.append(load_home_database, ignore_index = True)
    
    current_page = current_page+1
    
    
