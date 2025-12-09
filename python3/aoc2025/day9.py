import datetime

def calc_total(filename, part):

    with open("c:\\dev\\data\\aoc\\" + filename) as f:
        lines = f.read().splitlines()

    c = 0
    for line in lines:
        # print(line)
        pass

    print (filename, " -> about to return", c)
    return c

print (datetime.datetime.now(), ".. day 9 ..")
print (21 == calc_total("2025_day9t.txt", 1))
#print (1598 == calc_total("2025_day7.txt", 1))
#print (40 == calc_total("2025_day7t.txt", 2))
