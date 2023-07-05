input_num = int(input("please enter a number : "))
thisdict = dict()

for x in range(1,input_num+1):
    y = int(x)
    thisdict[x] = y*y
    
print(thisdict)