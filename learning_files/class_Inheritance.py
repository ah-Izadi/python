#create parent class
class Person:
    def __init__(self,fname,lname):
        self.x = fname
        self.y = lname

    def printname(self):
        print(self.x,self.y)

#create child class
# class Student(Person):
#     pass

# Person1 = Student("ali","ahmadi")
# Person1.printname()

#add __init__ function to child class
# try:
#     class Student(Person):
#         def __init__(self,fname,lname):
#             pass

#     Person1 = Student("ali","ahmadi")
#     Person1.printname()

# except AttributeError:
#     pass

#keep the inheritance of the parent's __init__() function
class Student(Person):
    def __init__(self,fname,lname):
        Person.__init__(self,fname,lname)

Person1 = Student("ali","ahmadi")
Person1.printname()

#Or Using super() Function
# class Student(Person):
#     def __init__(self,fname,lname):
#         super().__init__(fname,lname)

# Person1 = Student("ali","ahmadi")
# Person1.printname()

#Add a property to child class
# class Student(Person):
#     def __init__(self,fname,lname):
#         super().__init__(fname,lname)
#         self.birth = 2002

# Person1 = Student("ali","ahmadi")
# print(Person1.birth)

#Or
# class Student(Person):
#     def __init__(self,fname,lname,year):
#         # super().__init__(fname,lname)
#         self.birth = year

# Person1 = Student("ali","ahmadi",2002)
# print(Person1.birth)

#Add method to child class :
class Student(Person):
    def __init__(self,fname,lname,year):
        super().__init__(fname,lname)
        self.year = year
    def welcome(self):
            print("Welcome", self.x, self.y, "to the class of", self.year)

# Person1 = Student("ali","ahmadi",2002)
# Person1.welcome()