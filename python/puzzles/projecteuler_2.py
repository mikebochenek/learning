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

# New version demonstrating str.translate for character removal (lesser-known string method)
def f885_v2(n):
    if n <= 0:
        return 0
    s = str(n)
    # str.maketrans creates a translation table; here, we map '0' to None to remove it
    trans = str.maketrans('', '', '0')
    s_no_zero = s.translate(trans)
    # Sort the remaining digits and join back to string
    sorted_digits = ''.join(sorted(s_no_zero))
    return int(sorted_digits)

# Another version using list comprehension and functools.reduce for functional building of the number
from functools import reduce

def f885_v3(n):
    if n <= 0:
        return 0
    # List comprehension to filter non-zero digits, then sort
    digits = sorted([d for d in str(n) if d != '0'])
    # Use reduce to build the integer: start with 0, multiply by 10 and add each digit
    return reduce(lambda acc, d: acc * 10 + int(d), digits, 0)

def s885(n): # Let s(n) be the sum of f(d) for all positive integers d of n digits or less
    max = 10 ** n
    # print ('max', max)
    sum = 0
    for i in range (max):
        sum = sum + f885(i)
    ans = sum % 1123455689
    return sum

# Test cases for f885 variants
f885_test_cases = [
    (3403, 334),
    (100, 1),
    (102030, 123),
]

for func in [f885, f885_v2, f885_v3]:
    for input_val, expected in f885_test_cases:
        assert func(input_val) == expected

# Test cases for s885
s885_test_cases = [
    (1, 45),
    (5, 1543545675),
]

for input_val, expected in s885_test_cases:
    assert s885(input_val) == expected

# aha, this will never finish print (s885(18))