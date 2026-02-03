# https://www.johndcook.com/blog/2026/01/10/prime-chains/
from sympy import isprime

def chain_length(start, kind):
    p = start
    c = 0
    while isprime(p):
        c += 1
        p = 2*p + kind
    return c

print(chain_length(2759832934171386593519, 1))
print(chain_length(79910197721667870187016101, -1))