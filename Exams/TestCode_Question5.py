def myfunc(input_result):
    result = [x for x in input_result.split(" ")]

    x = " ".join(set(result))

    y = x.split(" ")
    y.sort()

    z = " ".join(y)
    return(z)

assert myfunc("hello world and practice makes perfect and hello world again") == "again and hello makes perfect practice world"

#Second Way
def myfunc(input_result):
    result = [x for x in input_result.split(" ")]
    return(" ".join(sorted(set(result))))

assert myfunc("hello world and practice makes perfect and hello world again") == "again and hello makes perfect practice world"