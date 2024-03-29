#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: mike  Created on Sat Jul  1 22:52:23 2023
"""

import array

def split(s, w, t):
    layers = int(len(s) / w / t)
    layers_size = int(len(s) / layers)
    zeros = array.array('i')
    ones = array.array('i')
    twos = array.array('i')
    for i in range(0, t):
        count0 = 0
        count1 = 0
        count2 = 0
        line = ''
        for j in range(0, w):
            for l in range(0, layers):
    
                #print (s[l*layers_size+i*w+j])
                if('0' == s[l*layers_size+i*w+j]):
                    count0 = count0 + 1
                    line = line + ' '
                    break
                if('1' == s[l*layers_size+i*w+j]):
                    count1 = count1 + 1
                    line = line + '8'
                    break
                if('2' == s[l*layers_size+i*w+j]):
                    count2 = count2 + 1
                    
            zeros.append(count0)
            ones.append(count1)
            twos.append(count2)

        print(line)

    #print(zeros)
    #print(len(s), layers, zeros, ones, twos)

    fewest = len(s)
    ans = 0
    for l in range(0, layers):
        if (fewest >= zeros[l]):
            fewest = zeros[l]
            ans = twos[l]*ones[l]
            #print(ans, l, fewest, ones[l], twos[l])

with open('/home/mike/Documents/aoc/2019/day_8.txt') as f:
    lines = f.read().splitlines()

#split('123456789012', 3, 2)
split('0222112222120000', 2, 2)
print('---\n')
split(lines[0], 25, 6)
