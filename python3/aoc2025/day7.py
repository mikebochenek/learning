import datetime

def calc_total(filename):
    total_cal_value = 0

    with open("c:\\dev\\data\\aoc\\" + filename) as f:
        lines = f.read().splitlines()

    c = 0
    i = [0] * len(lines[0])
    start = lines[0].find('S')
    i[start] = 1
    for line in lines:
        # print(line)
        if start != 0:
            #print ("first")
            start = 0
        else:
            for idy, y in enumerate(line):
                if (y == '.' and i[idy] == 1):
                    pass
                    # print ("pass", idy)
                if (y == '^' and i[idy] == 1):
                    # print ("split", idy)
                    c += 1
                    i[idy] = 0
                    i[idy-1] = 1
                    i[idy+1] = 1    



    print (datetime.datetime.now(), filename, " -> about to return", c)
    return c

print (21 == calc_total("2025_day7t.txt"))
print (1598 == calc_total("2025_day7.txt"))