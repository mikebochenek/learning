import re

def sum_points(filename):

    with open('/home/mike/ownCloud/Documents/aoc2023/'+filename+'.txt') as f:
        lines = f.read().splitlines()

    mysum = 0
    cards = [1] * 204 # here need to toggle between 6 and 204

    for idx, line in enumerate(lines):
        winning = [0] * 10
        d = line.split(':')[1].split('|')

        winning_s = d[0].strip().split(' ')
        c = 0
        for i, w in enumerate(winning_s):
            if (w != ''):
                winning[c] = int(w)
                c = c + 1

        c = 0
        you = d[1].strip().split(' ')
        for yi in you:
            if (yi != ''):
                y = int(yi)
                if (y in winning):
                    c = c + 1
                    #print('yes, found',y, winning)

        if (c > -1):
            copies = cards[idx]
            for i in range(c):
                cards[idx+i+1] = cards[idx+i+1] + copies
            #print ('line', idx, c, copies, cards)
            #sum = sum + (2 ** c)

        mysum = sum(cards)
        #print (winning, you)

    print ('sum-->', mysum)
    return mysum

print(sum_points('day4-0') == 13)

print(sum_points('day4-1'))  #6188 too low
