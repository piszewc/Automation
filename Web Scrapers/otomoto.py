# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 12:57:45 2018

@author: piotr
"""
import requests
from bs4 import BeautifulSoup
import pandas as pd 

scraped_cars = pd.DataFrame()



def only_main_page(url):
    for page in range (0,2):
        page+=1
        current_url = url+str(page)  
        print("Currenlty Working on page #: "+str(page))
        main_page_details(current_url)


def main_page_details(url):
    
    url = "https://www.otomoto.pl/osobowe/?page=1"  

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
    
    year_header = soup.select('.offer-item__content > .offer-item__params')
    years = ([link.find_all(attrs={"data-code": "year"}) for link in year_header])





    #create new pandas df
    s_car_title = pd.Series(car_title)
    s_car_link = pd.Series(car_link)
    s_price = pd.Series(price)
    s_years = pd.Series(years)
    
    car_df["car_title"] = s_car_title.values
    car_df["car_link"] = s_car_link.values
    car_df["car_price"] = s_price.values
    car_df["years"] = s_years.values

    scraped_cars = scraped_cars.append(car_df)

current_url = "https://www.otomoto.pl/osobowe/?page="  

only_main_page(current_url)

              
      