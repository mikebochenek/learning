def count(filename):

    with open('/home/mike/ownCloud/Documents/aoc2023/'+filename+'.txt') as f:
        lines = f.read().splitlines()

    for line in lines:
        min = 0
        print (line)
        for l in line:
            if (l == '/' or l == '\\'):
                1+1 #mirror
            if (l == '|' or l == '-'):
                1+1 #splitter
 
    return 0

print(count('day16-0') == 46)
# print(least('day16-1'))
