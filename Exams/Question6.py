user_input = input("enter the binery values : ").split(",")
result = []

for x in user_input:
    y = int(x,2)
    if y % 5 < 1:
        result.append(str(x))
    

print(", ".join(result))