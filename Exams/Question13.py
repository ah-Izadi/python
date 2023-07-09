class person:
    name = 1
    def __init__(self,name):
        self.name = name
    def prt(self):
        print(self.name)
obj = person(2)
obj.prt()
print(person.name)