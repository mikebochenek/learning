# https://www.johndcook.com/blog/2025/10/26/987654321/

num = lambda b: sum([k*b**(k-1) for k in range(1, b)])
denom = lambda b: sum([(b-k)*b**(k-1) for k in range(1, b)])

for b in range(3, 1001):
    n, d = num(b), denom(b)
    assert(n // d == b-2)
    assert(n % d == b-1)