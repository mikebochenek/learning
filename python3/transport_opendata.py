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


sample='http://transport.opendata.ch/v1/connections?from=Lausanne&to=Genève'
# sample='https://transport.opendata.ch/v1/connections?from=Zollikon&to=Stadelhofen'

data, duration = fetchurl(sample)
print ('(minimum)_duration:', duration, sample)
