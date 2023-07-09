class Person:
    def __init__(self,fname,lname):
        self.Firstname = fname
        self.Lastname = lname
    @classmethod
    def reset(cls):
        return cls("","")
    def __str__(self):
        return f"{self.Firstname} {self.Lastname}"
    
x = Person("ali","mohhamadi")
y = Person("mahmood","karimi")
x = Person.reset()
y = Person.reset()
print(x)
print(y)