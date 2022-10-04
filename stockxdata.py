#!/usr/bin/env python
# coding: utf-8

#STILL WORK IN PROGRESS

import requests
import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

#Using selenium go through the web page to retrieve all the href attributes for the products which we will use in our search function.

item_list = []
PATH = r"C:\Users\Playtech\Desktop\sele/chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.maximize_window()
for i in range(1,26):
    driver.get("https://stockx.com/search?s=dunk&page="+str(i))
    time.sleep(10)
    items = driver.find_elements(By.CSS_SELECTOR,'.css-1ibvugw-GridProductTileContainer [href]')
    
    for i in items:
        a_list.append(i.get_attribute('href').split("/")[-1])
        
#print(item_list)

#search for the product which will return all the data about the product stored inside Stockx's database.
"""def search(product):
    url = f'https://stockx.com/api/browse?_search={product}'
"""








