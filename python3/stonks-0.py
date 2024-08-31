#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 11:53:00 2024 based on https://algotrading101.com/learn/yahoo-finance-api-guide/
@author: mike
"""

import yfinance as yf
import logging

logging.basicConfig(level=logging.INFO,
    # filename="/tmp/app.log", # ideally https://docs.python.org/3/library/logging.handlers.html#logging.handlers.RotatingFileHandler
    format="{asctime} - {levelname} - {message}",
    style="{"
    )

def get_data(st): #get if it doesn't exist...
    d = yf.Ticker(st)
    logging.info(d.info)
    return d
    
# msft = get_data("MSFT")
nvda = get_data("NVDA")
ubsg = get_data("UBSG")
sdz  = get_data("SDZ")


