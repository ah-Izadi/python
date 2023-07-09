class Person:
    def __init__(self,age,name):
        self.age = age
        self.name = name
    
Human = Person("12","amirhossein")

print(Human.age+" "+Human.name)