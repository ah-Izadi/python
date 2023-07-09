class AccesStr:
        def __init__(self):
            pass
        def getStr(self):
            x=input("please enter Str : ")
            self.inpUser = str.upper(x)
        def printStr_upper(self):
            return(self.inpUser)



obj = AccesStr()
obj.getStr()
x=obj.printStr_upper()

    
assert x.isupper()