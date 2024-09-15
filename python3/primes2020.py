from datetime import datetime
import io
import requests
import unittest

''' totally unrelated..
startTime = datetime.now()
#url="https://raw.githubusercontent.com/cs109/2014_data/master/countries.csv"
url = "https://bochenek.ch/career/index.html"
s=requests.get(url).content
print (len(s), 'total bytes',
       datetime.now() - startTime, 'time taken to download career/index from bochenek.ch') # usually takes 0.11 to 0.25s
'''
def isPrime(x):
    #print ('checking', x)
    n = x**(1/2)
    for k in range(int(n)):
        if (x % (k+2) == 0):
            return False
    return True

startTime = datetime.now()

def myprint(o):
    print(o, end=', ')

def test_WithPrint():
    myprint(isPrime(4))
    myprint(isPrime(7))
    print(isPrime(25), end=', ')
    print(isPrime(983), end=', ')
    print(isPrime(23244)) # 23244 = 2 x 2 x 3 x 13 x 149

class TestPrimes(unittest.TestCase):
    def test_primes(self):
        testData = (3000761, 300001649, 5000001707, 50000000189, 500000001637, 999553561583, 99553561483) 
        for t in testData :  # http://compoasso.free.fr/primelistweb/page/prime/liste_online_en.php
            self.assertTrue(isPrime(t))
    def test_nonprimes(self):
        self.assertFalse(isPrime(256))
        self.assertFalse(isPrime(23244))

if __name__ == "__main__":  # has to be after 
    unittest.main()

# print(datetime.now() - startTime, 'time taken to calculate large primes') 