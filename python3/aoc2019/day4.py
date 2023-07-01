#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: mike - Created on Fri Jun 23 22:22:40 2023 
but somehow to lazy or can't think of code 
"""

def mc(i): #meets criteria?
    digits = 6

    # Two adjacent digits are the same (like 22 in 122345).
    adjacent = False
    
    # Going from left to right, the digits never decrease; they only ever increase or stay the same
    for j in range(0,digits-1):
        if (str(i)[j] > str(i)[j+1]):
            # print('digits decrease', i, j)
            return False
        if (str(i)[j] == str(i)[j+1]):
            adjacent = True

            # Part II below (breaks existing asserts)
            # the two adjacent matching digits are not part of a larger group of matching digits
            if (j < (digits-2) and str(i)[j+1] == str(i)[j+2]):
                adjacent = False
            if (j > 0 and str(i)[j+1] == str(i)[j-1]): #893 is too high still
                adjacent = False
                #print (i) -- anti-example: 779999
        
    return adjacent

#assert (mc(111111) and False == mc(223450) and False == mc(123789))
assert (mc(112233) and False == mc(123444) and mc(111122))

count = 0
for i in range(240298,784956): # 240298-784956
    if (mc(i)):
        count = count + 1
    
print ("count", count)
    
# https://cryptography.io/en/latest/ -- also crypto101 would be fun
from cryptography.fernet import Fernet
key = Fernet.generate_key()
print(key)

import hashlib
s = hashlib.sha256(b"https://docs.python.org/3/library/hashlib.html").hexdigest()

from hashlib import blake2b
s = blake2b(b'https://docs.python.org/3/library/hashlib.html#creating-hash-objects').hexdigest()
print (s)
