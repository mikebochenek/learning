# https://adventofcode.com/2020/day/4
# In your batch file, how many passports are valid?
import re
print ('starting day #4\n\n')

with open('/Users/mike/Documents/2020/aoc/day4.txt') as f:
    lines = f.read().splitlines()

valid = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']
haircolor = ['amb','blu','brn','gry','grn','hzl','oth']
required = valid.copy()
required.remove('cid')

def checkpassport(passport):
    props = passport.split()
    requiredCheck = required.copy()
    for p in props:
        s = p.split(':')
        if (s[0] == 'cid'):
            pass
        else:  # a little bit ugly but works seemingly...
            if s[0] == 'byr':
                if (int(s[1]) >= 1920) and (int(s[1]) <= 2002) :
                    requiredCheck.remove(s[0])
            elif s[0] == 'iyr':
                if (int(s[1]) >= 2010) and (int(s[1]) <= 2020) :
                    requiredCheck.remove(s[0])
            elif s[0] == 'eyr':
                if (int(s[1]) >= 2020) and (int(s[1]) <= 2030) :
                    requiredCheck.remove(s[0])
            elif s[0] == 'hgt':
                #print ('  trying hgt', s[1])
                if s[1].endswith('in'):
                    s[1]=s[1].replace('in','')
                    inches = int(s[1])
                    #print ('inches:', inches)
                    if (inches >= 59 and inches <= 76):
                        requiredCheck.remove(s[0])
                        #print ('valid in:', s[1])
                if s[1].endswith('cm'):
                    s[1]=s[1].replace('cm','')
                    cm = int(s[1])
                    #print ('cm:', cm)
                    if (cm >= 150 and cm <= 193):  # NB:  & is not the same as 'and'
                        requiredCheck.remove(s[0])
                        #print ('valid cm:', s[1])
                #else:
                    #print ('invalid: ', s[1])
            elif s[0] == 'hcl':
                #print ('hcl', s[1])
                if re.match(r"\#[0-9a-f]{6}", s[1]):
                    requiredCheck.remove(s[0])
                    #print ('   valid hcl', s[1])
                #else:
                    #print ('invalid: ', s[1])
            elif s[0] == 'ecl':
                if (s[1] in haircolor):
                    requiredCheck.remove(s[0])
                    #print ('   valid ecl', s[1])
                #else:
                    #print ('invalid: ', s[1])
            elif s[0] == 'pid':
                if re.match(r"[0-9]{9}", s[1]):
                    if len(s[1]) == 9:
                        requiredCheck.remove(s[0])
                        #print (s[1])
                #else:
                    #print ('invalid: ', s[1])
            else:
                assert(False) # should never get here!

            # https://adventofcode.com/2020/day/4#part2

    b = len(requiredCheck) == 0
    return b


globalCounter = 0
passport = ''
for l in lines:
    if len(l) == 0:
        if (checkpassport(passport)):
            globalCounter += 1
        passport = ''
    else:
        passport += ' ' + l

if (checkpassport(passport)):
    globalCounter += 1

print (globalCounter)