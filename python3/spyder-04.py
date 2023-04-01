#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created on Sun Mar 12 17:24:40 2023 to play around with requests API
import requests
from datetime import datetime
from bs4 import BeautifulSoup

startTime = datetime.now()

def fetchurl(URL):
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    
    images = soup.find_all("img") # https://pytutorial.com/how-to-get-all-images-beautifulsoup/
    for image in images:
        (image['src']) #remove print(..)

    print('surface', soup.findAll(text="Surface living:"))
    chf = soup.findAll(text="CHF")
    for c in chf:
        actualPrice = c.parent.find_next_sibling('span')
        print('CHF', actualPrice)
    
    results = soup.find(id="ResultsContainer") # https://realpython.com/beautiful-soup-web-scraper-python/
    print(len(page.text), 'bytes')


# fetchurl("https://realpython.github.io/fake-jobs/")

# I wonder how we can download images or gather other stats
fetchurl("https://www.homegate.ch/rent/3002739596")

# would it contain refs to images like this?
img1 = "https://media2.homegate.ch/f_auto/t_web_dp_large/listings/hau/3002739596/image/45133f8602fe3038dd8d9368e717c028.jpg"

fetchurl("https://www.homegate.ch/buy/3002696560")
img2 = "https://media2.homegate.ch/f_auto/t_web_320/listings/hgonif/3002752373/image/47b5475db5d2b8ab37e4cd616ce3f66e.jpg"

print(int((datetime.now() - startTime).total_seconds() * 1000), 'ms expired')