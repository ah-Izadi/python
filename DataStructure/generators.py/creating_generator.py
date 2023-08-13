from sys import getsizeof
y = [x*2 for x in range(10)]
gen = (x*2 for x in range(10))
print("list mem space: ",getsizeof(y))
print("Gen mem space: ",getsizeof(gen))
print(type(gen))