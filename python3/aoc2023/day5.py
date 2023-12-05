import re

# start Tue Dec  5 07:34:10 CET 2023

def lowest(filename):

    with open('/home/mike/ownCloud/Documents/aoc2023/'+filename+'.txt') as f:
        lines = f.read().splitlines()

    lowest = 0

    seeds = [0] * 20
    ss = lines[0].split(':')[1].split(' ')
    ss.remove('')
    for idx, s in enumerate(ss):
        if s != '':
            seeds[idx] = int(s)
    lines.remove(lines[0])

    #print (seeds)

    for idx, line in enumerate(lines):
        if 'map' in line:
            print (line)
        elif len(line) > 1:
            ss = line.split(' ')
            nums = [0] * len(ss)
            for idx, s in enumerate(ss):
                nums[idx] = int(s)
            # print(' -> ', nums)

    #print ('lowest-->', lowest)
    return lowest

print(lowest('day5-0') == 35)

# print(lowest('day5-1'))
