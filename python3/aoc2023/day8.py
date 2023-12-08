
# Fri Dec  8 07:27:34 CET 2023

def steps(filename):

    with open('/home/mike/ownCloud/Documents/aoc2023/'+filename+'.txt') as f:
        lines = f.read().splitlines()

    ins = lines[0]

    lines.remove(ins)
    lines.remove('')

    m = {} # map
    for line in lines:
        l = line.split('=')
        key = l[0].strip()
        value = l[1].strip()
        #print ('adding', key, value)
        m[key] = value

    #print (lines, m.keys())
    found = False
    count = 0
    p = 'AAA'
    while (found == False):
    #for count in range(0,len(ins)):
        current = m[p]
        #print (count, p, ' -> ', current)
        if (ins[count % len(ins)] == 'L'):
            p = current[1:4]
        if (ins[count % len(ins)] == 'R'):
            p = current[6:9]
        count += 1
        if (p == 'ZZZ'):
            found = True
            #print ('end!!', count)

    return count

print(steps('day8-0') == 2)
print(steps('day8-0b') == 6)
print('my answer', steps('day8-1'))
