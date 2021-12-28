# -*- coding: utf-8 -*-
"""
OtoDom Scraper created in order to help you create historical data for homes
"""

import requests
import pandas as pd
from bs4 import BeautifulSoup
from datetime import date
from datetime import datetime

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

def get_page_base(url, page_number):
    url = url+str(page_number)
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    
    #get non promoted items
    get_details = soup.select('div[data-cy="search.listing"]')[1]
    get_details = get_details.find('ul')

    main_page_dict = pd.DataFrame()

    for li in get_details.find_all("li", class_="css-7mmxt5 es62z2j30"):
        temp_dict = {}

        link = li.a['href']
        temp_dict['link'] = 'https://www.otodom.pl'+link
        
        title = li.find_all('h3')[0].text.strip()
        temp_dict['title'] = title

        location = li.select('article > p > span')[0].text.strip()
        temp_dict['location'] = location

        rooms = li.select('article > p > span')[1].text.strip()
        temp_dict['rooms'] = rooms

        price = li.select('article > p > span')[2].text.strip()
        temp_dict['price'] = price

        
        pricem2 = li.select('article > p > span')[3].text.strip()
        temp_dict['pricem2'] = pricem2

        space = li.select('article > p')[2].text.strip()
        temp_dict['space'] = space
        
        main_page_dict = main_page_dict.append(temp_dict,ignore_index=True)
        
    return main_page_dict

def get_last_page(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    soup = soup.find_all('script')
    soup = soup[1]
    
    jsonStr = soup.text.strip()
    index = soup.text.strip().find('"totalPages')
    jsonStr = jsonStr[index:]
    jsonStr = jsonStr.split(',')[0].strip()
    jsonStr = jsonStr.split(':')[1].strip()
    last_page = jsonStr.replace('"', '') 
    
    return int(last_page)

# Enter city link that you wish to scrape 

url = 'https://www.otodom.pl/pl/oferty/sprzedaz/mieszkanie/krakow'

start_time = datetime.now()
print("Start Time:", start_time)
print('Scraping Information for', url)


# get information about last page

end_page = get_last_page(url)
start_page = 1

final_table = pd.DataFrame()

for page_number in range(start_page, end_page+1):
    print('current page: ',page_number)
    final_table = final_table.append(get_page_base(url+'?page=', page_number),ignore_index=True)


date_today = date.today()
file_name = 'main_house_prices_'+str(date_today)+'.csv'
final_table.to_csv(file_name, encoding='utf-8-sig', index=False)

end_time = datetime.now()
total_time = end_time - start_time

print('End Time', end_time, 'We finsihed in:', total_time.total_seconds()/60, 'minutes')
print('File was saved localy as',file_name)









