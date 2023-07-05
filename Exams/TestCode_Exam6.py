def myfunc(user_input):
    result = [x for x in user_input.split(",")]
    result.sort()
    return(",".join(result))

assert myfunc("bag,hello,without,parrot") == "bag,hello,parrot,without"