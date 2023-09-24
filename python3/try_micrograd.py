# based on https://bernsteinbear.com/blog/compiling-ml-models/
# pip install micrograd         
from micrograd.nn import MLP
model = MLP(2, [4, 1])

print (model)

