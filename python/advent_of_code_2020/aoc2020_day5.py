# https://adventofcode.com/2020/day/5
print ('starting day #5...')

def decode(s):
    row = s[:7]
    row = row.replace('B','1')
    row = row.replace('F','0')
    col = s[-3:]
    col = col.replace('R','1')
    col = col.replace('L','0')
    r = int(row,2)
    c = int(col,2)
    seatId = r * 8 + c
    #print (s, row, col, r, c, seatId)
    return seatId

with open('/Users/mike/Documents/2020/aoc/day5.txt') as f:
    lines = f.read().splitlines()

maximum = 0
for l in lines:
    #print (l, decode(l))
    seatId = decode(l)
    if (seatId > maximum):
        maximum = seatId

print (maximum)

x = [0] * 1000
for l in lines:
    seatId = decode(l)
    x[seatId] = 1

for idx, xval in enumerate(x):
    if (xval == 0):
        print (idx,xval)
