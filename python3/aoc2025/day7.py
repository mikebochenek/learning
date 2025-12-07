import datetime

def calc_total(filename, part):
    total_cal_value = 0

    with open("c:\\dev\\data\\aoc\\" + filename) as f:
        lines = f.read().splitlines()

    c = 0
    if (part == 2):
        c = 1

    i = [0] * len(lines[0])
    start = lines[0].find('S')
    i[start] = 1
    for line in lines:
        # print(line)
        if start != 0:
            #print ("first")
            start = 0
        else:
            alt = 0
            for idy, y in enumerate(line):
                if (y == '.' and i[idy] == 1):
                    pass
                    # print ("pass", idy)
                if (y == '^' and i[idy] == 1):
                    # print ("split", idy)
                    if (part == 1):
                        c += 1
                        i[idy] = 0
                        i[idy-1] = 1
                        i[idy+1] = 1    
                    else: #part II
                        i[idy] = 0
                        if (i[idy-1] == 0):
                            i[idy-1] = 1
                            alt += 1
                        if (i[idy+1] == 0):    
                            i[idy+1] = 1    
                            alt += 1

            if (alt != 0 and part == 2):
                print ("split line=", line, "c=", c, "alt=", alt)
                c *= alt
            if (alt == 0 and part == 2):
                pass # print (i)

    print (filename, " -> about to return", c)
    return c

print (datetime.datetime.now(), ".. day 7 ..")
print (21 == calc_total("2025_day7t.txt", 1))
print (1598 == calc_total("2025_day7.txt", 1))
print (40 == calc_total("2025_day7t.txt", 2))
