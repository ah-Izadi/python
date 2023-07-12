class AgeException(Exception):
    pass

Age_Num = 18

try :
    input_num = int(input("please enter your age : "))
    if input_num < Age_Num:
        raise AgeException
    else:
        print("you can vote on this server :)")
    
except AgeException:
    print("your age is under 18 !!!")