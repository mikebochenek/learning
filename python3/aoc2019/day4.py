#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: mike - Created on Fri Jun 23 22:22:40 2023 
but somehow to lazy or can't think of code 
"""

def mc(i):
    if i == 111111:
        return True
    return False

assert (mc(111111) and False == mc(223450) and False == mc(123789))
# 240298-784956

for i in range(240298,784956):
    None
    
# https://cryptography.io/en/latest/ -- also crypto101 would be fun
from cryptography.fernet import Fernet
key = Fernet.generate_key()
print(key)

import hashlib
s = hashlib.sha256(b"https://docs.python.org/3/library/hashlib.html").hexdigest()

from hashlib import blake2b
s = blake2b(b'https://docs.python.org/3/library/hashlib.html#creating-hash-objects').hexdigest()
print (s)
