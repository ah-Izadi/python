mainList = []
#use append() method for Add item to list
mainList.append("apple")
mainList.append("banana")
mainList.append("cherry")
print(mainList)

#use insert method to add item in specified postion
mainList.insert(1,"waterMelon")
print(mainList)

#use extend methond to add two list together
secondList = ['orange']
FirstTuple = ('cocoa')
mainList.extend(secondList)
print(mainList)

#use plus(+) operator to add two list together
firstlist = ['apple']
secondlist = ['banana']
x = firstlist + secondlist
print(x)