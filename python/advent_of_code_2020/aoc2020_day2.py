# https://adventofcode.com/2020/day/2
# https://adventofcode.com/2020/day/2/input
# How many passwords are valid according to their policies?
print ('starting day #2...')

def isvalid(s):
    parts = s.split()
    #print (parts)
    assert (3 == len(parts)) # should always be 3
    
    range = parts[0].split('-')
    assert (2 == len(range)) # should always be 2
    min = int(range[0])
    max = int(range[1])
    
    letter = parts[1][0]
    str = parts[2]
    
    counter = str.count(letter) #https://www.geeksforgeeks.org/python-count-occurrences-of-a-character-in-string/

    print ('min:', min, ' max:', max, ' letter:', letter, ' str:', str, ' counter:', counter)

#    return (min <= counter & counter <= max)
    return bool(str[min-1] == letter) ^ bool(str[max-1] == letter)  # part 2 - incl. https://stackoverflow.com/questions/432842/how-do-you-get-the-logical-xor-of-two-variables-in-python

with open('/Users/mike/Documents/2020/aoc/passwords.txt') as f:
    lines = f.read().splitlines()

totalCount = 0
for l in lines:
    b = isvalid(l)
    print (b)
    if b:
        totalCount = totalCount + 1
    
print ('\n\n\n------------------')
print (lines)
print (totalCount)
