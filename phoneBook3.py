phoneDict = {"mahdi":9155027514 , "Ali":9359355157}
class phone:
    def __init__(self):
        pass

    def SetPhoneNum(name,phoneNum):
        if not phoneNum < 0:
            phoneDict[str(name)] = str(phoneNum)
            print(name," ",phoneDict[name])

    def findPhoneNum(Name):
            if Name.isdigit():
                try:
                    for x in phoneDict.keys():
                        if str(x) == Name:
                            return phoneDict[str(Name)]
                    for x in phoneDict.values():
                        if x is Name:
                            return phoneDict[Name]
                except KeyError or ValueError:
                    print("not found !!!")
            
            # elif Name.isdigit() and Name.isalpha():
            #     try:
            #         for x in phoneDict.keys():
            #             if x in Name:
            #                 return phoneDict[Name]
            #     except KeyError:
            #         print("not found !!!")
                    
            elif Name.isalpha():
                try:
                    for x in phoneDict.keys():
                        if x in Name:
                            return phoneDict[Name]
                except KeyError:
                    print("not found !!!")
    def Prt():
        return phoneDict

ph = phone

while True:
    Input_user = input("do you want go to Find PhoneNumber ? press 1\nor do you want go to Set PhoneNumber ? press 2 \ndo you want exit ? press 3\ndo you want Prt the phoneDict ? press 4\n : ")
    
    if Input_user == "2":
        print("*********************************************")
        ph.SetPhoneNum(input("please enter the name : "),int(input("please enter the PhoneNumber without 0 : ")))
        print("*********************************************")
        
    
    if Input_user == "1":
        print("*********************************************")
        print(ph.findPhoneNum(input("please enter the name : ")))
        print("*********************************************")
    
    if Input_user == "4":
        print("*********************************************")
        print(ph.Prt())
        print("*********************************************")
        
    if Input_user == "3" :
        print("*********************************************")
        break