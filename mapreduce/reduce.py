from functools import reduce
def add(x,y):
    return x + y

r = reduce(add,[1,2,3,4,5])

print(r)