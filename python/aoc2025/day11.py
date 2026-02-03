import datetime

def calc_total(filename, part):

    with open("c:\\dev\\data\\aoc\\" + filename) as f:
        lines = f.read().splitlines()

    c = 0
    for line in lines:
        s = line.split(":")
        paths = s[1].split(" ")
        print(s[0], " --> ", paths)
        pass

    print (filename, " -> about to return", c)
    return c

print (datetime.datetime.now(), ".. day 11 ..")
print (5 == calc_total("2025_day11t.txt", 1))
#print (1598 == calc_total("2025_day7.txt", 1))
#print (40 == calc_total("2025_day7t.txt", 2))

