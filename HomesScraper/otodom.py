# -*- coding: utf-8 -*-
"""
OtoDom Scraper created in order to help you create historical data for homes
"""

import requests
import pandas as pd
from bs4 import BeautifulSoup

# subpage
def scrape_subpage(url):
    url = 'https://www.otodom.pl/pl/oferta/nowe-wykonczone-2-pokojowe-mieszkanie-prywatnie-ID4eniw'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    
    scraper_values = pd.read_csv('otodom_values.csv', delimiter=';')
    
    main_list = []
    details_list = []
    add_list = []
    
    main_list = scraper_values[scraper_values['Location']=='Main'].values.tolist()
    details_list = scraper_values[scraper_values['Location']=='Details'].values.tolist()
    desciption_list = scraper_values[scraper_values['Location']=='Description'].values.tolist()
    add_list = scraper_values[scraper_values['Location']=='Additonal'].values.tolist()
    
    temp_dict = {}
    temp_table = pd.DataFrame()
    
    temp_dict['link'] = url
     
    for i in main_list:
        print("loading",i[0])
        get_mains = soup.select(i[1])[0]
        get_mains = get_mains.text.strip()
        temp_dict[i[0]] = get_mains
    
    for i in details_list:
        print("loading",i[0])
        new_value = i[1]+' > div'
        get_details = soup.select(new_value)[1]
        get_details = get_details.text.strip()
        temp_dict[i[0]] = get_details
    
    for i in desciption_list:
        print("loading",i[0])
        get_details = soup.select(i[1])
        get_details = get_details[0].text.strip()
        temp_dict[i[0]] = get_details
    
    for i in add_list:
        print("loading",i[0])
        new_value = i[1]+' > div'
        get_details = soup.select(new_value)[1]
        get_details = get_details.text.strip()
        temp_dict[i[0]] = get_details
        
    temp_table = temp_table.append(temp_dict,ignore_index=True)
    return temp_table


start_page = 1
max_page = 100
url = 'https://www.otodom.pl/pl/oferty/sprzedaz/mieszkanie/krakow?page='+str(start_page)
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

#get non promoted items
get_details = soup.select('div[data-cy="search.listing"]')

data1 = get_details.find('ul')
for li in data1.find_all("li"):
    print(li.text, end=" ")
    
print(get_details)
























