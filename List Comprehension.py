fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

#With list comprehension you can do all that with only one line of code:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)

new2 = []

for fruit in fruits:
    if "a" in fruit:
        new2.append(fruit)
print(new2)
#newlist = [expression for item in iterable if condition == True]

newlist = [x.title() for x in fruits]
print(newlist)