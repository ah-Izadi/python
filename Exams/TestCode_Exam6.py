alphabet = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"
result = []

def myfunc(user_input):
    Edited_user_input = user_input.split(",")
    for x in alphabet:
        for y in Edited_user_input:
            if y.startswith(x):
                result.append(y)
    return(result)

assert myfunc("bag,hello,without") == ['bag', 'hello', 'without']