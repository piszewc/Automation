# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 12:57:45 2018

@author: piotr
"""
import requests
from bs4 import BeautifulSoup
import pandas as pd 



def only_main_page(url):
    for page in range (0,1000):
        page+=1
        current_url = url+str(page)  
        print("Currenlty Working on page #: "+str(page))
        main_page_details(current_url)

def main_page_details(url):
    
    scraped_cars = pd.DataFrame()
    
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    all_cars = soup.find_all('article')
    
    car_df = pd.DataFrame()
    car_list = []

    main_header = soup.select('.offer-item__content > .offer-item__title > .offer-title > a')
    car_title = ([link['title'].strip() for link in main_header])
    car_link = ([link['href'].strip() for link in main_header])

    price_header = soup.select('.offer-item__content > .offer-item__price > .offer-price > .offer-price__number')
    price = ([link.get_text().strip() for link in price_header])
    
    year_header = soup.find_all(attrs={"data-code": "year"})
    year_list = []
    for i in year_header:
        i = str(i)
        year_list.append(str(i[60:64]))
    
    #create new pandas df
    s_car_title = pd.Series(car_title)
    s_car_link = pd.Series(car_link)
    s_price = pd.Series(price)
    s_years = pd.Series(year_list)
    
    car_df["car_title"] = s_car_title.values
    car_df["car_link"] = s_car_link.values
    car_df["car_price"] = s_price.values
    
    car_df['car_price'], car_df['currency'] = car_df['car_price'].str.split('  ', 1).str
    car_df['car_price'] = car_df['car_price'].str.strip()
    car_df['currency'] = car_df['currency'].str.strip()

    car_df["years"] = s_years.values
    #car_df['years'] = car_df['years'].map(lambda x: x.lstrip('+-').rstrip('aAbBcC'))
   
    car_df.to_csv("car_database.csv", mode='a', header=True, encoding='utf-8', index=False)


current_url = "https://www.otomoto.pl/osobowe/?page="  

only_main_page(current_url)
