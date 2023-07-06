result = list()
for x in range(1000,3001):
    z = str(x)
    if int(z[0]) % 2 == 0 and int(z[1]) % 2 == 0 and int(z[2]) % 2 == 0 and int(z[3]) % 2 == 0:
        result.append(z)
Str_result = ",".join(result)
print(Str_result)