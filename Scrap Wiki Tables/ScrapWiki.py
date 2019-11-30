# -*- coding: utf-8 -*-
"""
Created by
https://github.com/piszewc/

Scrap Wiki will scrap all Wiki tables from selected Page.
All tables are going to be saved to CSV file in current location.

"""

import requests
import pandas as pd
from bs4 import BeautifulSoup

page_html = "https://en.wikipedia.org/wiki/List_of_best-selling_singles"

page = requests.get(page_html).text
soup = BeautifulSoup(page, "lxml")
data = []

table = soup.find('table', {'class':'wikitable sortable'})
table_body = table.find('tbody')

header = table_body.find_all('th')
header = [header.text.strip() for header in header]

count_tables = soup.find_all('table')

rows = table_body.find_all('tr')
for row in rows:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    data.append([ele for ele in cols if ele]) # Get rid of empty values

data[0] = header
dftable = pd.DataFrame(data[1:], columns=data[0])

site = pd.read_html(page_html)[0]