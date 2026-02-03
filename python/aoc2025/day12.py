import datetime

def calc_total(filename, part):

    with open("c:\\dev\\data\\aoc\\" + filename) as f:
        lines = f.read().splitlines()

    c = 0
    for line in lines:
        if (':' in line):
            pass
        elif (' ' in line):
            pass
        else:
            print(line)

    print (filename, " -> about to return", c)
    return c

print (datetime.datetime.now(), ".. day 12 ..")
print (2 == calc_total("2025_day12t.txt", 1))
#print (0 == calc_total("2025_day7.txt", 1))
#print (0 == calc_total("2025_day7t.txt", 2))

