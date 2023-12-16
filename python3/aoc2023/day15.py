# start part I Sat Dec 16 14:08:23 CET 2023
# done  part I Sat Dec 16 14:20:49 CET 2023

def weirdhash(str):
    cv = 0
    for s in str:
        cv += ord(s)
        cv *= 17
        cv = cv % 256

        #print (s, cv)

    return cv

def seqsum(filename):

    with open('/home/mike/ownCloud/Documents/aoc2023/'+filename+'.txt') as f:
        lines = f.read().splitlines()

    mysum = 0

    m = {} # map
    for line in lines:
        l = line.split(',')
        for s in l:

            mysum += weirdhash(s)

            key = s[0].strip()
            value = s[1].strip()
            # print ('adding', key, value)

    print (filename, '->', mysum)
    return mysum

print(weirdhash('HASH'))
print(seqsum('day15-0') == 1320)
print(seqsum('day15-1'))
