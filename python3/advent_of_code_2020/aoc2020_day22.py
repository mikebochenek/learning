# https://adventofcode.com/2020/day/22 

#with open('data/day22-test.txt') as f:
with open('data/day22.txt') as f:
    lines = f.read().splitlines()

#d1 = lines[1:6]
#d2 = lines[8:13]
d1 = lines[1:26]
d2 = lines[28:53]
rnd = 0

while (len(d1) > 0 and len(d2) > 0):
    rnd += 1
    print ('---- round #', rnd)
    print ('player 1 now has:', d1)
    print ('player 2 now has:', d2)

    p1 = d1[0]
    print ('player 1 plays', p1)

    p2 = d2[0]
    print ('player 2 plays', p2)

    d1 = d1[1:len(d1)]
    d2 = d2[1:len(d2)]
    if (int(p1) > int(p2)):
        d1.append(p1)
        d1.append(p2)
        print ('player 1 wins\n')
    if (int(p2) > int(p1)):
        d2.append(p2)
        d2.append(p1)
        print ('player 2 wins\n')

winner = d1
if (len(d1) == 0):
    winner = d2

score = 0
for i, x in enumerate(winner):
    score += int(x) * (len(winner)-i)

print ('score: ', score)
