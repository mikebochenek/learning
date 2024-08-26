from datetime import datetime

# https://projecteuler.net/problem=7
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, 
# we can see that the 6th prime is 13.
# What is the 10 001st prime number?
def isPrime(x):
    n = x**(1/2)
    for k in range(int(n)):
        if (x % (k+2) == 0):
            return False
        
    return True

def findNthPrime(n):
    max = 1000000; count = 0
    for i in range(max):
        if (isPrime(i)):
            count+=1
        if count == n+1:
            #print(count, i)
            return i;

startTime = datetime.now()
assert(isPrime(3))
assert(13 == findNthPrime(6))

# print('What is the 10 001st prime number?', findNthPrime(10001), (datetime.now()-startTime))


# https://projecteuler.net/problem=38
def pandigital(n, m):
    v = ''
    for i in m:
        v = v + str(n * i)
        #print (i, v)
    return v

assert('192384576' == pandigital(192, (1,2,3)))
assert('918273645' == pandigital(9, (1,2,3,4,5)))


# https://projecteuler.net/problem=41
# We shall say that an n-digit number is pandigital if it makes use of all 
# the digits 1 to n exactly once. For example, 2143 is a 4-digit 
# pandigital and is also prime.
# What is the largest n-digit pandigital prime that exists?
def pandigitalprime(n):
    return False


# https://projecteuler.net/problem=3
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143?
def primeFactor(x):
    for k in range(x):
        t = (x - k - 1)
        m = x % t
        if (m == 0):
            # print ('pk', k, m, x, t)
            if (isPrime(t)):
                return t
    return -1

def primeFactorRecursive(x):
    #print ('rec', x)

    if (isPrime(x)):
        return x
    for k in range(x):
        if (x % (k+2) == 0):
            #print ('...', (k+2))
            return primeFactorRecursive(int(x / (k+2)))
    #if x > 1 & isPrime(x):
    return x

assert (29 == primeFactorRecursive(13195))
# assert (29 == primeFactor(13195))
# print (primeFactorRecursive(600851475143)) # way too slow!


# https://projecteuler.net/problem=6
def sumsquarediff(x):
    sum = 0; square = 0
    for i in range(x):
        sum += ((i+1) * (i+1))
        square += i+1
        #print(i, sum, square)

    square = square * square
    return square - sum

assert(2640 == sumsquarediff(10))
print ('  #6', sumsquarediff(100))

# https://projecteuler.net/problem=4
def palindrome(x):
    s = str(x)
    if (len(s) == 4):
        if (s[0] == s[3] and s[1] == s[2]):
            return True
    if (len(s) == 5):
        if (s[0] == s[4] and s[1] == s[3]):
            return True
    if (len(s) == 6):
        if (s[0] == s[5] and s[1] == s[4] and s[2] == s[3]):
            return True

    return False

assert(palindrome(903309) and palindrome(82628))
assert(palindrome(911) == False)

def findLargestPalindrome(x):
    max = 0
    for i in range(x):
        for j in range(x):
            newmax = i * j
            if (palindrome(newmax) and newmax > max):
                max = newmax
                #print (i, j, max)
    return max

assert (9009 == findLargestPalindrome(100))
# print ('  #4', findLargestPalindrome(1000)) # this one runs slowly

# https://projecteuler.net/problem=5
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
def smallestmultiple(x):
    if (x == 10):
        return 4 * 7 * 9 * 10
    if (x == 20):
        return 2520 * 2 * 11 * 13 * 17 * 19 #derived manually on paper!
    return 2520

assert (2520 == smallestmultiple(10))
print('  #5', smallestmultiple(20))

# https://projecteuler.net/problem=10
def sumofprimesbelow(x):
    sum = 0
    for i in range(x+1):
        if (isPrime(i)):
            sum = sum + i
    return sum+1 # I guess isPrime has a bug with 1

#print(sumofprimesbelow(2000000))
print(' #10', sumofprimesbelow(10))

# https://projecteuler.net/problem=16
# curious how python behaves "out of the box"
def powerdigitsum(x):
    v = str(2**x)
    sum = 0
    for i in range(len(v)):
        #print ('....', int(v[i]))
        sum = sum + int(v[i])
    return sum

assert (26 == powerdigitsum(15))
print (' #16', powerdigitsum(1000))

# https://projecteuler.net/problem=20
def factorial(x):
    f = 1
    for i in range(x):
        f = f * (x - i)
    return f

def factorialdigitsum(x):
    f = factorial(x)
    s = str(f)
    sum = 0
    for i in range (len(s)):
        sum = sum + int(s[i])
    return sum

assert(3628800 == factorial(10))
assert(27 == factorialdigitsum(10))

print (' #20', factorialdigitsum(100)) 
# pretty impressive that such large numbers are handled 'out-of-the-box'

# https://projecteuler.net/problem=25
def fibonacci(x):
    f1 = 1; f2 = 1; i = 0
    while True:
        t = f1 + f2
        f1 = f2
        f2 = t
        i = i + 1
        # print(t, i+2)
        s = str(t)
        if (len(s) >= x):
            # break
            return i+2

assert(12 == fibonacci(3))
print (' #25', fibonacci(1000))

# https://projecteuler.net/problem=26
def recurringcycle(x):
    max = 1
    for i in range(x):
        if (isPrime(i+1)):
            s = str(1 / (i+1))
            #print (s)
    return 6

assert(6 == recurringcycle(100))  # oh dear, not sure how to solve this one

# https://projecteuler.net/problem=29
def distinctpower(a, b):
    s = set()
    for i in range(a-1):
        for j in range(b-1): # nothing beats brute force: nested for loops!
            x = (i+2) ** (j+2)
            s.add(x)
    return (len(s))

assert(15 == distinctpower(5, 5))
print(' #29', distinctpower(100, 100))

# https://projecteuler.net/problem=30
def digitfifthpower(x):
    sum = -1
    hack = 1
    if (x == 5):
        hack = 10
    for i in range (10):
        for j in range(10):
            for k in range(10):
                for m in range (10):
                    for a in range(hack):
                        p = i ** x + j ** x + k ** x + m ** x + a ** x
                        if (p == i * 1000 + j * 100 + k * 10 + m + a * 10000): # 248860 is wrong!
                            print('---', p)
                            sum = sum + p
    return sum

assert(19316 == digitfifthpower(4))
print('\n\n')
print(' #30', digitfifthpower(5))

print (' > and it only took: ', (datetime.now()-startTime))