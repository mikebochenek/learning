# based on https://bernsteinbear.com/blog/compiling-ml-models/
# pip install micrograd         
from micrograd.nn import MLP
model = MLP(2, [4, 1])

print (model)

# millennium brainteaser
def f(n):
    if n <= 1:
        return 1/6
    else:
        return f(n-1) + (1 + 1 / (n*(4*n-1)*(4*n-2)) )

def g(n):
    if n <= 1:
        return 1/30
    else:
        return g(n-1) + (1 + 1 / (n*(4*n+1)*(4*n+2)) )

print (f(2024) + 3 - g(2024))