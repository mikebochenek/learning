'''
https://www.bochenek.ch/blog/coding/2015/05/13/collatz-conjecture/
The Collatz Conjecture is defined as follows: Given a positive integer n, 
if it is odd then calculate 3n+1. If it is even, calculate n/2. 
Repeat this process with the resulting value. 
'''

def calc(n):
    if n <= 1:
        print ('4, 2, 1, ...')
    elif n % 2 == 0:
        print (int(n), end=', ') # https://stackoverflow.com/questions/493386/how-to-print-without-newline-or-space
        calc(n/2)
    else:
        print (int(n), end=', ') # https://stackoverflow.com/questions/13097099/how-to-make-python-print-1-as-opposed-to-1-0
        calc(3 * n + 1)
    
print (calc (1))

for x in range(6):
    calc (x)

'''
https://projecteuler.net/problem=3
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
'''

