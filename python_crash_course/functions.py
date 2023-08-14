# default Values
def test(name = 'wili'):
    print(name)

test()
test('hamed')

# return simple value
def test():
    return 'hello'
print(test())

# passing a list 
def test(list):
    return list[0]

print(test(['salam','khoobi']))

#modify a list in function
def test(r,list = [1,2,3,4,5,6,7,8,9,10]):
    list.remove(r)
    return list

print(test(r=2))

#Arbitary arguments
def test(*x):
    print(x)

test(1,2,3,4,5,6,7,8,9)

#arbitary keyword argument
def test(**arg):
    print(arg['lname'])
    
y = test(lname = 10)
