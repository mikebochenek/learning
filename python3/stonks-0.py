#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 11:53:00 2024 based on https://algotrading101.com/learn/yahoo-finance-api-guide/
@author: mike
"""

import yfinance as yf
import logging
import pickle
import platform
import os
from datetime import datetime

logging.basicConfig(level=logging.INFO,
    # filename="/tmp/app.log", # ideally https://docs.python.org/3/library/logging.handlers.html#logging.handlers.RotatingFileHandler
    format="{asctime} - {levelname} - {message}",
    style="{"
    )

# https://machinelearningmastery.com/a-gentle-introduction-to-serialization-for-python/
# neat thing about stack-overflow coding, is that one discovers interesting areas of the web...
def get_data(st): #get if it doesn't exist - pickle serialization
    if ('Windows' == platform.system()):
        path = 'C:/Users/mike/Documents/opendata/ticker/'
    else:
        path = '/home/mike/Documents/opendata/ticker/'
    pickle_filename = path + st + '.pickle'

    if (os.path.isfile(pickle_filename)):
        logging.info('load local ticker cache' + pickle_filename)
        with open(pickle_filename, "rb") as infile:
            ticker_reconstructed = pickle.load(infile)
            return ticker_reconstructed
    else:
        d = yf.Ticker(st)
        # logging.info(d.info)
        hist = d.history(period="6mo") # https://pypi.org/project/yfinance/#quick-start
        # logging.info(type(hist)) # <class 'pandas.core.frame.DataFrame'>

        with open(pickle_filename , "wb") as outfile:
            pickle.dump(hist, outfile)
            logging.info('save to local pickle cache' + pickle_filename)

        return d
    
startTime = datetime.now()

msft = get_data("MSFT")
nvda = get_data("NVDA")
ubsg = get_data("UBSG")
sdz  = get_data("SDZ")

# logging.info(msft)
logging.info(' ->> all done: ' + str(datetime.now() - startTime)) 
