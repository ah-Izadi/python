result = []

def myfunc(user_input):
    for x in user_input.split(","):
        result.append(x)

    result.sort()

    return(",".join(result))

assert myfunc("bag,hello,without,parrot") == "bag,hello,parrot,without"