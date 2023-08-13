#use clear() method to remove all elements in list
clearList = ['apple','banana','cherry']
clearList.clear()
print(clearList)

#use pop() method to remove the element in specified position
clearList2 = ['apple','banana','cherry']
clearList2.pop(0)
print(clearList2)

#use remove() method to remove specified element from list
clearList2.remove("banana")
print(clearList2)

#or 
clearList3 = ['apple','banana','cherry']
clearList3[0]= ''
print(clearList3)