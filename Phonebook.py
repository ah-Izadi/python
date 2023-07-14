phoneDict = {}

class phone:
    def __init__(self,name,phoneNum):
        self.name = name
        self.phoneNum = phoneNum
        
    def SetPhoneNum(self):
        if not self.phoneNum < 0:
            phoneDict[self.name] = self.phoneNum
            return(phoneDict)

    def findPhoneNum(self,Name):
        if phoneDict[Name]:
            return("0" + str(phoneDict[Name]))
        else:
            return("this name was not difined !!!!!!!")
            
            
p1 = phone(input("please enter the name : "),int(input("please enter the PhoneNumber without 0 : ")))
print(p1.SetPhoneNum())
print(p1.findPhoneNum(input("please enter the name : ")))