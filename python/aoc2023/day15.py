# start part I Sat Dec 16 14:08:23 CET 2023
# done  part I Sat Dec 16 14:20:49 CET 2023
# start part 2 Sat Dec 16 20:34:50 CET 2023
# done  part 2 Sat Dec 16 21:46:16 CET 2023
import re

def weirdhash(str):
    cv = 0
    for s in str:
        cv += ord(s)
        cv *= 17
        cv = cv % 256
    return cv

def seqsum(filename):

    with open('/home/mike/ownCloud/Documents/aoc2023/'+filename+'.txt') as f:
        lines = f.read().splitlines()

    lens = [""] * (256)

    for line in lines:
        l = line.split(',')
        for s in l:
            n = 0
            if (s[len(s)-1]=='-'):
                key = s[:len(s)-1]
                n = weirdhash(key)
                #print (s, 'clearly has an - ...', key, n)
                if (key in lens[n]):
                    #print('TODO yes,need to remove')
                    # lens[n] = lens[n].replace(key, '')
                    lens[n] = re.sub('.'+key+'..', '', lens[n])
                    # NB: before, I was doing only key+'..' but forgetting the extra space
            else:
                key = s.split("=")[0]
                valu= s.split("=")[1]
                n = weirdhash(key)
                #print (s, '   does not ==>', key, valu, n)
                if (key in lens[n]):
                    #print('1+1  # TODO clever replacement')
                    lens[n] = re.sub(key+'=.', s, lens[n])
                else:
                    lens[n] = lens[n] + ' ' + s

            if 1==2:
                print ('After ', s, ':', n)
                for idx, b in enumerate(lens):
                    if (len(b.strip()) > 0):
                        print (' Box', idx, '[', b.strip(), ']')

    mysum = 0
    for idx, b in enumerate(lens):
        if (len(b.strip()) > 0):
            #print (' Box', idx, '[', b.strip(), ']')
            box = b.strip()
            bstring = box.split(" ")
            for bidx, blens in enumerate(bstring):
                if ("=" in blens):
                    v = (idx+1) * (bidx+1) * int(blens.split("=")[1]) 
                else:
                    print('some error: definitively blank space', idx, bidx, '[', blens, ']')
                
                #print ('...',v)
                mysum += v
 
    return mysum

#print(weirdhash('HASH'))
print(seqsum('day15-0') == 145) #1320)
print(seqsum('day15-1'))

# 389762 your answer is too high (21:31:30)
# 279470 correct (21:45:13) - found bug with blank space
