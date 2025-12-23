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
        path = 'C:/Users/User/Documents/opendata/ticker/'
    else:
        path = '/home/mike/Documents/opendata/ticker/'
    pickle_filename = path + st + '.pickle'

    if (os.path.isfile(pickle_filename)):
        logging.info('<-- LOAD local ticker cache: ' + pickle_filename)
        with open(pickle_filename, "rb") as infile:
            ticker_reconstructed = pickle.load(infile)
            return ticker_reconstructed
    else:
        d = yf.Ticker(st)
        hist = d.history(period="max") # https://pypi.org/project/yfinance/#quick-start
        # Value Meaning "1d" 1 day "5d" Last 5 days "1mo" Last 1 month "3mo" Last 3 months "6mo" Last 6 months
        #  "1y" 1 year "2y" 2 years "5y" 5 years "10y" 10 years 
        # "ytd" From January 1st this year "max" All available historical data
        # logging.info(type(hist)) # <class 'pandas.core.frame.DataFrame'>
        # logging.info(d.info)

        with open(pickle_filename , "wb") as outfile:
            pickle.dump(hist, outfile)
            logging.info('--> SAVE to local pickle cache: ' + pickle_filename)

        return d
    
startTime = datetime.now()

msft = get_data("MSFT")
nvda = get_data("NVDA")
ubsg = get_data("UBS")
btc  = get_data("BTC-USD") # https://finance.yahoo.com/quote/BTC-USD/
sol  = get_data("SOL-USD") # https://finance.yahoo.com/quote/SOL-USD/
eth  = get_data("ETH")
cad  = get_data("CHFCAD=X")
jpy  = get_data("CHFJPY=X")

# logging.info(msft)
logging.info('\t ->> all done: ' + str(datetime.now() - startTime)) 
