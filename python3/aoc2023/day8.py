
# Fri Dec  8 07:27:34 CET 2023

def steps(filename):

    with open('/home/mike/ownCloud/Documents/aoc2023/'+filename+'.txt') as f:
        lines = f.read().splitlines()

    ins = lines[0]

    lines.remove(ins)
    lines.remove('')

    m = {} # map
    sset = set()
    for line in lines:
        l = line.split('=')
        key = l[0].strip()
        value = l[1].strip()
        #print ('adding', key, value)
        if (key[2] == 'A'):
            sset.add(key)
        m[key] = value

    s = list(sset)
    print (' --> ', len(s), s) #, lines, m.keys())
    count = 0
    # p = '11A'
    found = 0
    while (found <= len(s) and count <= 600):
    #for count in range(0,len(ins)):
        found = 0
        new_s = list(s)
        for idx, p in enumerate(s):

            current = m[p]
            direction = ins[int(count / len(s)) % len(ins)] 
            #print (count, p, ' -> ', current)
            if (direction == 'L'):
                p = current[1:4]
            if (direction == 'R'):
                p = current[6:9]
            count += 1

            new_s[idx] = p

            if (p[2] == 'Z'):
                found += 1
            if (found >= len(s)):
                print ('end!!', count)
                return (count) / len(s)

            if (count % 1 == 0 or found > 1):
                print (count, idx, s, direction, current, p, found)

        s = new_s

    return (count-1) / len(s)

#print(steps('day8-0') == 2)
#print(steps('day8-0b') == 6)
print(steps('day8-0c') == 6)
# print('my answer', steps('day8-1'))

# my answer 3.8333333333333335

# 4 --> That's not the right answer. I
