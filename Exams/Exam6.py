user_input = input("please enter the words : ")
result = [x for x in user_input.split(",")]

result.sort()

print(",".join(result))