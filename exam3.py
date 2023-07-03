y = []
def my_func(a,b):
    for x in range(a,b):
        if x % 7 == 0 and x % 5 != 0:
            y.append(str(x))
    
    return(", ".join(y))
    
assert my_func(0,22) == "7, 14, 21"
assert my_func(0,30) == "7, 14, 21"
assert my_func(0,10) == "7, 14, 21"
assert my_func(10,20) == "7, 14, 21"
assert my_func(22,22) == "7, 14, 21"
