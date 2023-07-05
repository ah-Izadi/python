user_input = input("please enter the words : ")
result = []

for x in user_input.split(","):
    result.append(x)

result.sort()

print(",".join(result))