# https://projecteuler.net/problem=885

def f885(n):
    if n <= 0:
        return 0
    s_n = str(n)
    digits = []
    for s in s_n: # kinda brute force
        if (s != '0'):
            digits.append(s) 
    digits.sort()
    s_n = ''.join(digits) # convert digits list into a string
    return int(s_n) # return integer     # print (digits, s_n)  

def s885(n): # Let s(n) be the sum of f(d) for all positive integers d of n digits or less
    max = 10 ** n
    # print ('max', max)
    sum = 0
    for i in range (max):
        sum = sum + f885(i)
    ans = sum % 1123455689
    return sum

assert (334 == (f885(3403)))
assert (45 == s885(1)) # should be 45
assert (1543545675 == s885(5)) # should be 1543545675
print (s885(18))