thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict.values():
  print(x)
  
  #loop keys
  print("\n")
  for x in thisdict.keys():
    print(x)
    
#loop items
for x, y in thisdict.items():
  print(x, y)
