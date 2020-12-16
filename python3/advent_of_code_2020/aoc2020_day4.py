# https://adventofcode.com/2020/day/4
# Starting at the top-left corner of your map and following a slope of right 3 and down 1, how many trees would you encounter?
print ('starting day #4')

with open('/Users/mike/Documents/2020/aoc/day4-test.txt') as f:
    lines = f.read().splitlines()

passport = ''
for l in lines:
    if l == '':
        print (passport)
    else:
        passport.join(l)

print (lines)
