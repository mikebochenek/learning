import re

def spe_range(str):
    for s in str:
        if spe(s):
            return True
    return False

def spe(c): #ial
    if str(c).isdigit() or c == '.':
        return False
    else:
        #print ('special!', c)
        return True

def sum_parts(filename):

    with open('/Users/mike/ownCloud/Documents/aoc2023/'+filename+'.txt') as f:
        lines = f.read().splitlines()

    sum = 0

    for idx, line in enumerate(lines):
        nums = re.findall('\d+', line)
        #print (nums)
        for n in nums:
            i = line.index(n)
            #print (idx, i, n, line)

            touching = False

            #print ('try ', line[i-1])
            if (i > 0 and spe(line[i-1])):
                touching = True
                #print ('  touching left', n)

            #print ('try right', line[i+len(n)], 'inbounds', (i + len(n)) < len(line))
            if ((i + len(n)) < len(line) and spe(line[i+len(n)])):
                touching = True
                #print ('  touching right', n)


            start_pad = -1
            end_pad = 1
            if (i == 0):
                start_pad = 0
            if (i == len(line)):
                end_pad = 0
            
            fromm = i+start_pad
            to = i+len(n)+end_pad
            str = lines[idx-1][fromm:to]
            #print ('try above?', str, fromm, to)
            if (idx > 0 and spe_range(str)):
                touching = True
                #print ('  touching above', n)

            #print(idx < len(lines), idx, len(lines))
            if (idx+1 < len(lines) and spe_range(lines[idx+1][fromm:to])):
                touching = True
                #print ('  touching below', n)

            if touching:
                sum = sum + int(n)

    print ('sum-->', sum)
    return sum

print(sum_parts('day3-0') == 4361)

#print(spe('*'))
#print(spe('%'))
#print(spe('$'))
#print(spe('.'))

print(sum_parts('day3-1')) # 543466 is too low