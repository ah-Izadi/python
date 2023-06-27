list1 = ["banana","apple","chery","banana"]

list1.remove("banana")

print(list1)

list1.remove("banana")

print(list1)

# I have an idea!


for fruit in list1:
    if "banana" in fruit :
        list1.remove(fruit)
        
print(list1)