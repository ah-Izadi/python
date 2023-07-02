def myfunc(*kids):
    print("the youngest child is " + kids[1])
    
myfunc("amir","ali","hossein")

#Arbitary keyword arguments
def func(**kids):
    print("the youngest child is " + kids["lname"])
    
func(fname = "ali" , lname = "ahmadi")
