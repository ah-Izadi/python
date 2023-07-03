y = []
for x in range(2000,3201):
    if x % 7 == 0 and x % 5 != 0:
        y.append(str(x))
 
print(", ".join(y))