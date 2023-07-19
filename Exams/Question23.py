thisTuple = (1,2,3,4,5,6,7,8,9,10)
underFive = []
belowFive = []
for x in thisTuple:
    if x <= 5:
        underFive.append(str(x))
    
    elif x > 5:
        belowFive.append(str(x))
        
print(",".join(underFive))
print(",".join(belowFive))