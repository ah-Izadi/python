# input_num = int(input("please enter a number : "))
thisdict = dict()

def my_func(input_numT):
    thisdict = dict()
    for x in range(1,input_numT+1):
        y = int(x)
        thisdict[x] = y*y
    return thisdict
    
print(thisdict)
assert my_func(5) == {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
assert my_func(3) == {1: 1, 2: 4, 3: 9}
assert my_func(4) == {1: 1, 2: 4, 3: 9, 4: 16}