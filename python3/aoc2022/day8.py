#!/usr/bin/env python3

def countv(name):
    with open('/home/mike/Documents/aoc/2022/'+name+'.txt') as f:
        lines = f.read().splitlines()

    count = 0
    l = len(lines)
    for idx, x in enumerate(lines):
        line = (lines[idx])
        for idy, y in enumerate(line):
            # print (y)

            if (idx == 0 or idy == 0): # edge
                count+=1

            # from left
            for x in range(0, idy):
                if (y < line[x]):
                    break # definitively wrong

            # from right

            # from top

            # from bottom
    
    print ('count', count)
    return 21

assert(21==countv('day8-0'))
#print('my puzzle', countv('day8-1'))