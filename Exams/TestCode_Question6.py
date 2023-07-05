result = []

def myfunc(user_input):
    for x in user_input.split(","):
        y = int(x,2)
        if y % 5 < 1:
            result.append(str(x))
    
    return(", ".join(result))

assert myfunc("0100,0011,1010,1001") == "1010"