for x in range(2000,3201):
    if x % 7 > 0:
        continue
    if x % 5 < 1:
        continue
    print(x,end=',')