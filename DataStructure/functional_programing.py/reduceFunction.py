#reduce()

from functools import reduce

nums = [1,2,3,4,5,6,7,8,9]

def add(a, b):
    return a + b

print(reduce(add,nums))