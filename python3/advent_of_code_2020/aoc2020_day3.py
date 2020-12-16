# https://adventofcode.com/2020/day/3
# https://adventofcode.com/2020/day/3/input
# Starting at the top-left corner of your map and following a slope of right 3 and down 1, how many trees would you encounter?
print ('starting day #3')

with open('/Users/mike/Documents/2020/aoc/day3.txt') as f:
    lines = f.read().splitlines()

count = 0
for idx, line in enumerate(lines):
    h = (3*idx) % (len(line))
    #print (idx+1, h, line[h], line)
    if ('#' == line[h]):
        count = count + 1

# part 2: What do you get if you multiply together the number of trees encountered on each of the listed slopes?
count = 0; count1 = 0; count2 = 0; count3 = 0; count4 = 0
for idx, line in enumerate(lines):
    if ('#' == line[(1*idx) % (len(line))]): # Right 1, down 1.
        count = count + 1
    if ('#' == line[(3*idx) % (len(line))]): # Right 3, down 1. (This is the slope you already checked.)
        count1 = count1 + 1
    if ('#' == line[(5*idx) % (len(line))]): # Right 5, down 1.
        count2 = count2 + 1
    if ('#' == line[(7*idx) % (len(line))]): # Right 7, down 1.
        count3 = count3 + 1
    if (idx % 2 == 0): # Right 1, down 2.
        if (('#' == line[int(idx/2) % (len(line))])):
            count4 = count4 + 1
            #print (idx, line)
    
print (count, count1, count2, count3, count4)
print (count * count1 * count2 * count3 * count4)
