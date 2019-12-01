# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 21:23:56 2019

@author: goto
"""
import requests
import pandas as pd
from bs4 import BeautifulSoup

class website(object):
    def __init__(self,url):
        self.url = url
        
class scrapper(website):
    def __init__(self,url):
        website.__init__(self, url)
    
    def save_csv(tables):
        
        table_number = 0 
        
        for table in tables:
            file_name = "test"+str(table_number)+".csv"
            table.to_csv(file_name,index=False)  
            table_number = table_number+1      
        
    def create_table_df(url):
        current_tables = pd.read_html(url)
        scrapper.save_csv(current_tables)
        
    def get_header_name(url):
        pass
    
 
    
    
    
    
scrapper.create_table_df("https://en.wikipedia.org/wiki/List_of_best-selling_singles")
