a = 40
b = 70
c = 200

if b > a :
    print("b gearter than a !")
    
elif a > b:
    print("a greater than b !")
    
else : 
    print("a and b are equal")
    


#Short hand if 
if a > b : print("a gearter than b")

#Short hand if ... else
print("a") if a > b else print("b")

# AND operator
if a < b and b < c :
    print("both conditions are true")
    
# OR operator 
if a > b or a < c:
  print("At least one of the conditions is True")
  
# NOT operator 
if not a > b:
  print("a is NOT greater than b")
  
# Nested if statment
x = 15

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")
    
# PASS statment
if b > a:
  pass