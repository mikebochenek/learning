# https://projecteuler.net/problem=885

def f885(n):
    s_n = str(n)
    digits = []
    for s in s_n: # kinda brute force
        if (s != '0'):
            digits.append(s) 
    digits.sort()
    s_n = ''.join(digits) # convert digits list into a string
    return int(s_n) # return integer     # print (digits, s_n)  

def s885(n):
    ans = 1 % 1123455689
    return ans

assert (334 == (f885(3403)))
print (s885(1)) # should be 45
print (s885(5)) # should be 1543545675