# -*- coding: utf-8 -*-
"""
Following Scrip will download data from Wiki Pages
"""

import requests
import pandas as pd

page = requests.get("https://en.wikipedia.org/wiki/List_of_universities_in_the_United_Kingdom_by_enrolment").text

from bs4 import BeautifulSoup

soup = BeautifulSoup(page, "lxml")
data = []

table = soup.find('table', {'class':'wikitable sortable'})
table_body = table.find('tbody')

header = table_body.find_all('th')
header = [header.text.strip() for header in header]

rows = table_body.find_all('tr')
for row in rows:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    data.append([ele for ele in cols if ele]) # Get rid of empty values

data[0]=header

dftable = pd.DataFrame(data[1:], columns=data[0])
