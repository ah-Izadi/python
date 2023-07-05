input_result = input("please enter :")
result = [x for x in input_result.split(" ")]

x = " ".join(set(result))

y = x.split(" ")
y.sort()

z = " ".join(y)
print(z)



#second way
input_result = input("please enter :")
result = [x for x in input_result.split(" ")]
print(" ".join(sorted(set(result))))