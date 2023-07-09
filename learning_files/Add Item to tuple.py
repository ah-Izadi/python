# 1 _ Convert tuple to list , append "orange" to list and convert it back into tuple
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

print(thistuple)

# 2 _ create new tuple and add it to main tuple
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple) 
