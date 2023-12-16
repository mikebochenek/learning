
def hash(filename):

    with open('/home/mike/ownCloud/Documents/aoc2023/'+filename+'.txt') as f:
        lines = f.read().splitlines()

    sum = 0

    m = {} # map
    for line in lines:
        l = line.split(',')
        for s in l:
            key = s[0].strip()
            value = s[1].strip()
            print ('adding', key, value)


    return sum / len(s)

print(hash('day15-0') == 1320)
