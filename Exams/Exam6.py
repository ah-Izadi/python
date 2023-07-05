alphabet = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"
user_input = input("please enter the words : ")
result = []

Edited_user_input = user_input.split(",")

for x in alphabet:
    for y in Edited_user_input:
        if y.startswith(x):
            result.append(y)

print(result)