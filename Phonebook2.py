

while True:
    phoneDict = {"mahdi":9155027514 , "Ali":9359355157}
    
    user_Menu = input("do you want go to Find PhoneNumber ? press 1\nor do you want go to Set PhoneNumber ? press 2 \n1do you want exit ? press 3\n : ")
    
    def SetPhoneNum(name,phoneNum):
        if not phoneNum < 0:
            phoneDict[name] = phoneNum
            print(phoneDict[name])

    def findPhoneNum(Name):
        try:
            if phoneDict[Name]:
                print("0" + str(phoneDict[Name]))
        except KeyError:
            print("this phoneNumber was not difined !!!")

    def Menu():
        if user_Menu == "2":
            SetPhoneNum(input("please enter the name : "),int(input("please enter the PhoneNumber without 0 : ")))
        if user_Menu == "1":
            findPhoneNum(input("please enter the name : "))
    
    if user_Menu == "3":
        break

    Menu()