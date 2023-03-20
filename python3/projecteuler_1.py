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

print('What is the 10 001st prime number?', findNthPrime(10001), (datetime.now()-startTime))


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
assert (29 == primeFactor(13195))
print (primeFactorRecursive(600851475143)) # way too slow!