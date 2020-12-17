print ('starting day 7 of AOC 2020...') # https://adventofcode.com/2020/day/7

class Bag:
    def __init__(self, color, count):
        self.color = color 
        self.count = count
        self.subbags = list()
    def addBag(self, newBag):
        self.subbags.append(newBag)
    def contains(self, colors):
        for sb in self.subbags:
            for color in colors:
                if sb.color == color:
                    return True
        return False

with open('/Users/mike/Documents/2020/aoc/day7.txt') as f:
    lines = f.read().splitlines()

bagRules = []
for l in lines:
    w = l.split()
    bag = Bag(w[0]+w[1], 1)
    assert(w[2] == 'bags')
    assert(w[3] == 'contain')
    if (w[4] == 'no' and w[5] == 'other' and w[6] == 'bags.'):
        pass # print ('--- ignore rule:', l)
    else:
        print ('-----------', bag.color)
        for i in range(4, (len(w)-3), 4):
            count = w[i]
            color = w[i+1]+w[i+2]
            assert(w[i+3]=='bags,' or w[i+3]=='bags.' or w[i+3]=='bag,' or w[i+3]=='bag.')
            print ('   i: ', i, 'count:', count, '   color:', color)
            bag.addBag(Bag(color, count))
    
    bagRules.append(bag)

count = 0
delta = -1
colors = {'shinygold'} #we really want a set, not a list
while count != delta:
    delta = len(colors) - 1
    for b in bagRules:
        if (b.contains(colors)):
            if (b.color in colors):
                pass
            else:
                count += 1
                colors.add(b.color)
                print ('found', colors)
    
print (len(lines), len(bagRules), count, delta) # part 1 answer was 229!
