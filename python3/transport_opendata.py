#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  9 14:41:33 2024 
https://transport.opendata.ch/docs.html
https://github.com/OpendataCH/Transport/blob/master/web/examples/connections.php

@author: mike
"""
import requests
import json
from datetime import datetime

locations = [8576202, # Zollikon, Felbenstrasse
    8503059, # Zürich Stadelhofen, Bahnhof
    "8591329"] # "Zürich, Saalsporthalle" 

## TODO: would be nice to do lazy-fetch (saving locally, also for debugging..)
def fetchurl(URL):
    page = requests.get(URL)
    connection_data = json.loads(page.text)
    
    # print(json.dumps(connection_data, indent=4))
    
    minimum_duration = 1000;
    for c in connection_data.get('connections'):
        d = c.get('duration')
        m = datetime.strptime(d[3:], '%H:%M:%S')
        print (' _ minute:', m.minute)
        
        if (m.minute < minimum_duration):
            minimum_duration = m.minute
        
    return connection_data, minimum_duration

def fetchurl_S(URL):
    page = requests.get(URL)
    connection_data = json.loads(page.text)
    min_duration = connection_data.get('min_duration');
    print ('min_duration:', min_duration)
    return min_duration / 60

# sample='http://transport.opendata.ch/v1/connections?from=Lausanne&to=Genève'
# sample='https://transport.opendata.ch/v1/connections?from=Zollikon&to=Stadelhofen'
# sample='https://transport.opendata.ch/v1/connections?from='+str(locations[2])+'&to='+str(locations[0])
# data, duration = fetchurl(sample)

sample = 'https://search.ch/timetable/api/route.json?from=Zollikon,Gustav-Maurer-str+15A&to=Z%C3%BCrich,+Uetlibergstrasse.+231'
duration = fetchurl_S(sample)
print ('(minimum)_duration:', duration, sample)

# or is this even better?
# https://search.ch/timetable/api/route.json?from=Einsiedeln&to=Z%C3%BCrich,+F%C3%B6rrlibuckstr.+60

# http://transport.opendata.ch/v1/locations?type=address&query=Z%C3%BCrich,+F%C3%B6rrlibuckstr.+60
