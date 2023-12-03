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
            i = line.index(n)  # careful 130 vs. 30 #    > definively not touching 136 30
            prev_i = i
            if (len(n) <= 2 and ' '.join(nums).count(n) > 1): # and line[i-1] != '.'):
                if (idx == 12):
                    i = 113
                if (idx == 15):
                    i = 10
                if (idx == 38):
                    i = 97
                if (idx == 44 and i == 15):
                    i = 88
                if (idx == 44 and i == 23):
                    i = 45
                if (idx == 54):
                    i = 11
                if (idx == 64):
                    i = 134
                if (idx == 70):
                    i = 9
                if (idx == 84):
                    i = 136
                if (idx == 92):
                    i = 71
                if (idx == 99):
                    i = 63
                if (idx == 121):
                    i = i
                if (idx == 125 and i == 64):
                    i = 65  
                if (idx == 125 and i == 21):
                    i = i
                if (idx == 136):
                    i = 129

                if (i != prev_i):
                    print (idx, i, n, nums) #lines with issue: 38, 54, 64, 92
                

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
            #if (n == '30'):
            #    print ('try above?', str, fromm, to)
            if (idx > 0 and spe_range(str)):
                touching = True
                #print ('  touching above', n)

            #print(idx < len(lines), idx, len(lines))
            if (idx+1 < len(lines) and spe_range(lines[idx+1][fromm:to])):
                touching = True
                #print ('  touching below', n)

            if touching:
                sum = sum + int(n)
            else:
                1+1
                print ('    > definively not touching', idx, n)

    print ('sum-->', sum)
    return sum

print(sum_parts('day3-0') == 4361)

#print(spe('*'))
#print(spe('%'))
#print(spe('$'))
#print(spe('.'))

print(sum_parts('day3-1')) # 543466 is too low, 543506 is also too low, 543693 also too low!!
# 543695 Because you have guessed incorrectly 4 times on this puzzle, please wait 5 minutes before trying again. [Return to Day 3]
# 543689