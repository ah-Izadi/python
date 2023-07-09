class Person:
    head = 1
    def __init__(self,name,age):
        self.name = name
        self.age = age

x = Person("ali",36)
y = Person("ahmad",16)

x.head = 3
print(x.head)

print(Person.head)

#instance attribute

x.family = "izadi"
print(x.family)
try:
    print(y.family)
except AttributeError:
    print("AttributeError")