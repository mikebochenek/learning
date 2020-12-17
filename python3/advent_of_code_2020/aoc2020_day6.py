# https://adventofcode.com/2020/day/6
import string
print ('starting day #6\n\n')

with open('/Users/mike/Documents/2020/aoc/day6-test.txt') as f:
    lines = f.read().splitlines()

def countYes_part1(s):
    count = 0
    for c in string.ascii_lowercase:
        if (s.find(c) > 0):
            count += 1

    return count

def countYes(s):
    count = 0
    participants = len(s.split())
    for c in string.ascii_lowercase:
        if (s.count(c) == participants):
            count += 1

    return count


total = 0
a = ''
for l in lines:
    if len(l) == 0:
        total += countYes (a)
        a = ''
    else:
        a += ' ' + l

total += countYes (a)

print (total)

