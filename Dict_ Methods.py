main_dict = {"Favorite_fruit" : "WaterMelon" , "Favorite_Food" : "spaghetti" , "Favorite_Drink" : "water"}


#clear() method remove all elements of dictionary
main_dict.clear()
print(main_dict)


#again restore dict for tests
main_dict = {"Favorite_fruit" : "WaterMelon" , "Favorite_Food" : "spaghetti" , "Favorite_Drink" : "water"}


#copy() method return copy of dictionary
copy_dict = main_dict.copy()
print(copy_dict)


#fromkeys() method Create a dictionary with the specified keys and value
keys = "key1" , "key2" , "key3"
value = "0"
test_dict = dict.fromkeys(keys,value)
print(test_dict)


#get() method returns value of specified key
print(main_dict.get("Favorite_fruit"))


#items() method Returns a list containing a tuple for each key value pair
print(main_dict.items())


#keys() method return a list containing dictionary keys
print(main_dict.keys())


#pop() method remove element of specified key
main_dict.pop("Favorite_Food")
print(main_dict)


#popitem() method remove last value in dict
main_dict.popitem()
print(main_dict)


#setdefult() method return the value of specified key , if key does not exists insert the key with specified value
main_dict.setdefault("Favorite_Food","Spaghetti") 
print(main_dict)


#update() method update the dictionary with specified kay and value pair
main_dict.update({"Favorite_Drink" : "water"})
print(main_dict)


#values() method return a list of dict values
print(main_dict.values())

