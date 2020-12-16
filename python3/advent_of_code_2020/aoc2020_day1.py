print ('starting day 1 of AOC 2020...') # https://adventofcode.com/2020/day/1/input

with open('/tmp/numbers.txt') as f:
    lines = f.read().splitlines()

for n in lines:
    for m in lines:
        i = int (m)
        j = int (n)
        if (i + j == 2020):
            print (i * j)
        
print (lines)

for n in lines:
    for m in lines:
        for l in lines:
            i = int (m)
            j = int (n)
            k = int (l)
            if (i + j + k == 2020):
                print (i * j * k)
        
print (lines)