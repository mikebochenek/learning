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