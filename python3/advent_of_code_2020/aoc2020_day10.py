# https://adventofcode.com/2020/day/10 - --- Day 10: Adapter Array ---
# print ('starting day #10 (after skipping some days)...')

with open('/Users/mike/Documents/2020/aoc/day10.txt') as f:
    lines = f.read().splitlines()

numbers = []
for l in lines:
    numbers.append(int(l))
numbers.sort()

diff1=0
diff2=0
diff3=0

prev=0
for n in numbers:
    diff = n - prev
    prev = n
    if (diff == 1):
        diff1 += 1
    if (diff == 2):
        diff2 += 1
    if (diff == 3):
        diff3 += 1

diff3 +=1 #for the last one - because it's always 3..

print (numbers)
print (diff1, diff2, diff3)
print (diff1 * diff3)
print ('\n\n------------part 2---------\n\n')

d = [None] * len(numbers)
prev = 0
for idx, n in enumerate(numbers):
    d[idx] = n - prev
    prev = n
print (d)


stringRep = str(d)
countOption0 = stringRep.count('1, 1, 1, 1')
countOption1 = stringRep.count('3, 1, 1, 1, 3,')
countOption2 = stringRep.count('3, 1, 1, 3,')
print (countOption0, countOption1, countOption2)
print ((7 ** countOption0) * (4 ** countOption1) * (2 ** countOption2))
# ok the options and the '7' came from some reverse engineering..