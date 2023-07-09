class Person:
    def __init__(self,age,name):
        self.age = age
        self.name = name
    
    def __str__(self):
        return f"{self.name}({self.age})"

Person_Object = Person(36,"Ali")
print(Person_Object)