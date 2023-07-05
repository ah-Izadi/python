def myfunc(input_nums):
    return(input_nums.split(","))
assert myfunc("10,20,30,40") == ['10', '20', '30', '40']

def myfunc(input_nums):
    return(tuple(input_nums.split(",")))
assert myfunc("10,20,30,40") == ('10', '20', '30', '40')