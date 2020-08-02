# Make sure you install these modules with pip if you don't have them
import time
import re
import lxml.html
import requests
# You will need to have Chrome and Chrome webdriver installed. The webdriver needs to be in your path
from selenium import webdriver
import collections
import pandas as pd
from selenium.webdriver.common.by import By


TAG_RE = re.compile(r'<[^>]+>')
file = open('nationlinks.html',"r")
html = file.read()
doc = lxml.html.fromstring(html)
urls = doc.xpath("//a[contains(@class, 'nlink')]/@href")
browser = webdriver.Chrome()
browser.get('https://www.nationstates.net')
# You have 15 seconds to sign into the browser once it opens
time.sleep(15)
for i in urls:
    urlparttwo = str(i)
    url = 'https://www.nationstates.net/' + urlparttwo
    browser.get(url)
    checkbutton = browser.execute_script('return document.querySelector("#content > div.unbox > form > p > button").innerHTML')
    if re.search (r'Withdraw', checkbutton, re.IGNORECASE) is None:
            zabutton = browser.find_element(By.XPATH, '/html/body/div[3]/div/div[11]/form/p/button')
            zabutton.click()
    else:
            print("Hmm maybe that one is already saved")
    
browser.quit()
