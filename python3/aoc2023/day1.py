
def spelled_digit(s):
    digits = ['#!', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    for idx, d in enumerate(digits):
        if s.startswith(d):
            return idx
    return -1

def calc_total(filename):

    with open('/Users/mike/Documents/aoc2023/'+filename+'.txt') as f:
        lines = f.read().splitlines()

    total_cal_value = 0
    for line in lines:
        first = -1
        last = -1
        for idx, c in enumerate(line):
            spelled = spelled_digit(line[idx:])
            if c.isdigit() or spelled > 0:

                if c.isdigit():
                    last = int(c)
                    if (first < 0):
                        first = int(c)
                else:
                    last = spelled
                    if (first < 0):
                        first = spelled

        cal_value = first * 10 + last
        total_cal_value += cal_value

    print (filename, total_cal_value)
    #print (lines)

#calc_total('day1-0')
calc_total('day1-1')
calc_total('day1-2')