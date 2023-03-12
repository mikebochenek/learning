#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created on Sun Mar 12 17:24:40 2023 to play around with requests API

import requests
from datetime import datetime
from bs4 import BeautifulSoup

startTime = datetime.now()
URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="ResultsContainer") # https://realpython.com/beautiful-soup-web-scraper-python/

print(datetime.now() - startTime, len(page.text))