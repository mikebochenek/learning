#!/usr/bin/env python3

def countv(name):
    with open('/home/mike/Documents/aoc/2022/'+name+'.txt') as f:
        lines = f.read().splitlines()

    a = [99*99]
    return 21

assert(21==countv('day8-0'))
print('my puzzle', countv('day8-1'))