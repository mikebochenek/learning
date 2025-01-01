#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  9 14:41:33 2024 
https://transport.opendata.ch/docs.html
https://github.com/OpendataCH/Transport/blob/master/web/examples/connections.php
http://transport.opendata.ch/v1/locations?type=address&query=Z%C3%BCrich,+F%C3%B6rrlibuckstr.+60

or alternative:
https://search.ch/timetable/api/route.json?from=Einsiedeln&to=Z%C3%BCrich,+F%C3%B6rrlibuckstr.+60

@author: mike
"""
import requests
import json
import sys
import platform
from datetime import datetime

locations = [8576202, # Zollikon, Felbenstrasse
    8503059, # Zürich Stadelhofen, Bahnhof
    8591329] # "Zürich, Saalsporthalle" 

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
    #print ('min_duration:', min_duration)
    return int(min_duration / 60)

# sample='http://transport.opendata.ch/v1/connections?from=Lausanne&to=Genève'
# sample='https://transport.opendata.ch/v1/connections?from=Zollikon&to=Stadelhofen'
# sample='https://transport.opendata.ch/v1/connections?from='+str(locations[2])+'&to='+str(locations[0])
# data, duration = fetchurl(sample)

start = 'Zollikon,Gustav-Maurer-str+15A' # default 
start = 'Güetlistrasse 24, 8620 Wetzikon'
if len(sys.argv) > 1:
    start = sys.argv[1]
#sample = 'https://search.ch/timetable/api/route.json?from='+start+'&to=Z%C3%BCrich,+Uetlibergstrasse.+231'
#duration = fetchurl_S(sample)
#print ('(minimum)_duration:', duration, sample)

destinations = ['Minervastrasse 14, Zürich',
    'Zürich, Therese-Giehse-Str. 6',
    'Rämistrasse 101, Zürich',
    'Bleulerstrasse 49, 8008 Zürich',
    'Uetlibergstrasse 231, 8045 Zürich',
    'Flurstrasse 68,8048 Zürich']

final_list = []
print ('  start:', start)
startTime = datetime.now()
for dest in destinations:
    sample = 'https://search.ch/timetable/api/route.json?from='+start+'&to='+dest
    duration = fetchurl_S(sample)
    print ('  (minimum)_duration:', duration, dest)
    final_list.append(duration)

print ('\n', final_list, int((datetime.now() - startTime).total_seconds() * 1000), 
    'ms expired, on', platform.system(), platform.release())
