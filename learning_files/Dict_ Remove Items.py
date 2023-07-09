mydict = {"model" : "Pride" , "brand" : "Saipa" , "Car operation" : "300,000 km","year" : "1388"}

# pop() method
mydict.pop("model")
print(mydict)

#popitem() method
mydict.popitem()
print(mydict)

#del function
del mydict["brand"]
print(mydict)

mydict = {"model" : "Pride" , "brand" : "Saipa" , "Car operation" : "300,000 km","year" : "1388"}

#clear() Method
mydict.clear()
print(mydict)

#del Function
del mydict
print(mydict)