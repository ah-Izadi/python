# class PhoneNumber:
#     def __init__(self,phoneNum):
#         self.PhoneNumSetter(phoneNum)
#         self.phone = phoneNum
    
#     def PhoneNumGetter(self):
#         return self.phone
        
#     def PhoneNumSetter(self,value):
#         if value < 0:
#             print("phone number cannot less than ZERO !!! ")
#         else:
#             self.phone = value

#     phoneNumber = property(
#         fget=PhoneNumGetter,
#         fset=PhoneNumSetter,
#     )

# PHONE = PhoneNumber(-6323721233)


class PhoneNumber:
    def __init__(self,phoneNum):
        self.phoneNum=phoneNum
        # self.phoneNum = phoneNum
    
    @property
    def phoneNum(self):
        return self.phoneNum
    
    # @phoneNumber.getter
    # def PhoneNumGetter(self):
    #     return self.phoneNum
    
    @phoneNum.setter    
    def phoneNum(self,value):
        if value < 0:
            print("phone number cannot less than ZERO !!! ")
        else:
            self.j=phoneNum = value


PHONE = PhoneNumber(345)