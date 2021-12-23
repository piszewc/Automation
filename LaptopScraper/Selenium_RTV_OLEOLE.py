# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from selenium import webdriver #import webdriver - launch browser
from selenium.webdriver.common.by import By # search using specific parameters.
from selenium.webdriver.support.ui import WebDriverWait #wait for a page to load. 
from selenium.webdriver.support import expected_conditions as EC #wait for specific element to be loaded.
from selenium.common.exceptions import TimeoutException # timeout errors
import pandas as pd

options = webdriver.ChromeOptions()
#options.add_argument("--incognito")
driver = webdriver.Chrome("./chromedriver.exe",options=options)
driver.get("https://www.oleole.pl/") # only works with https or http

# Wait 20 seconds for page to load
timeout = 20

try:
    WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "h1[id='logo']")))
except TimeoutException:
    print("Timed out waiting for page to load") 
    driver.quit()
    
# find search button and type searched item
    
search_bar = driver.find_element_by_css_selector("input[id='keyword']")
search_bar.click()

search_bar.send_keys("lenovo legion 5")
#click on search button
driver.find_element_by_css_selector("a[class='selenium-search-button']").click()

items_prices = pd.DataFrame(columns=["Title","Price"])

# find all titles from page
items_titles = driver.find_elements_by_css_selector("div[class='product-box js-UA-product ']")


for i in items_titles:
    title = i.find_elements_by_css_selector("h2[class='product-name']")[0].text
    
    try:
        price = i.find_elements_by_css_selector("div[class='price-normal selenium-price-normal']")[0].text
    except:
        price = "NaN"
        
    items_prices = items_prices.append(pd.DataFrame({"Title":title,"Price":price}, index=[0]))


