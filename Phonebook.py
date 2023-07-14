phoneDict = {}

class phone:
    def __init__(self,name,phoneNum):
        self.name = name
        self.phoneNum = phoneNum

class SetPhoneNum(phone):
    def SetPhoneNum(self):
        if not self.phoneNum < 0:
            phoneDict[self.name] = self.phoneNum
            return phoneDict
class Find:
    def __init__(self,Name):
        self.Name = Name
        # phone.__init__(self,name,phoneNum)
    def findPhoneNum(self):
        if phoneDict[self.Name]:
            print(phoneDict[self.Name])
        else:
            print("this name was not difined !!!!!!!")

p1 = SetPhoneNum(input("please enter the name : "),int(input("please enter the PhoneNumber without 0 : ")))
print(p1.SetPhoneNum())
find = Find(input("please enter the name that you want find phoneNum :"))
print(find.findPhoneNum())