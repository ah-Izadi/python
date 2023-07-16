from colorama import Fore
class phone:
    def __init__(self,phoneDict):
        self.phoneDict = phoneDict

    def SetPhoneNum(self,contactName,phoneNum):
        if not phoneNum < 0:
                self.phoneDict[str(contactName)] = str(phoneNum)
                print(Fore.GREEN + contactName,": ",self.phoneDict[contactName])

    def findPhoneNum(self,userInput):
        
            keys = list(self.phoneDict.keys())
            values = list(self.phoneDict.values())
            flag = False
            for char in userInput: 
                if char.isdigit():
                    flag = True
            if flag:        
                for k, v in self.phoneDict.items():
                    if v in values:
                        print("*********************************************")
                        print(Fore.BLUE +" contact name is: "+ k+", and it`s phone Number is: "+v)

            elif not flag:        
                for k, v in self.phoneDict.items():
                    if k in keys:
                        print("*********************************************")
                        print(Fore.BLUE +" contact name is: "+ k+", and it`s phone Number is: "+v)
                        
    def Prt(self):
        return self.phoneDict

ph = phone(phoneDict={})

while True:
    Input_user = input(Fore.GREEN + "1 = Search user or number:\n2 = save a new contact:\n3 = show contacts and phoneNumbers:\n4 = EXIT:\n ")
    
    if Input_user == "2":
        print(Fore.LIGHTYELLOW_EX + "*********************************************")
        ph.SetPhoneNum(input(Fore.BLUE + "please enter the name : "),int(input(Fore.GREEN + "please enter the PhoneNumber without 0 : ")))
        print(Fore.LIGHTBLUE_EX + "*********************************************")
        
    
    if Input_user == "1":
        print(Fore.BLUE + "*********************************************")
        ph.findPhoneNum(input(Fore.LIGHTMAGENTA_EX + "please enter the name or Phone Number : "))
        print(Fore.RED + "*********************************************")
    
    if Input_user == "3":
        print(Fore.LIGHTRED_EX + "*********************************************")
        print(Fore.GREEN + ph.Prt())
        print(Fore.LIGHTYELLOW_EX + "*********************************************")
    
    if Input_user == "4":
        print("*********************************************")
        break