LIST1 = ["banana","apple","cherry"]

#loop trough a list
for x in LIST1 :
    print(x)
    
print("\n")
    
#break Statment
for x in LIST1:
    if x == "apple":
        break
    print(x)
    
print("\n")

#Continue statment
for x in LIST1:
    if x in "apple":
        continue
    print(x)
    
print("\n")

#Loop trough a String 
for x in "apple":
    print(x)
    
print("\n")

#using range() function
for x in range(6):
    print(x)
    
print("\n")

#Using the start parameter:
for x in range(1, 6):
  print(x)
  
print("\n")

#Increment the sequence with 3 (default is 1):
for x in range(2, 30, 3):
  print(x)
  
print("\n")

#Print all numbers from 0 to 5, and print a message when the loop has ended:
for x in range(6):
  print(x)
else:
  print("Finally finished!")
  
print("\n")

#Nested loops
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
  for y in fruits:
    print(x, y)
    
print("\n")

#pass statment
for x in [0, 1, 2]:
  pass
