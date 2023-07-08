from operator import itemgetter
l = []

while True:
    inp = input()
    if not inp:
        break
    l.append(tuple(inp.split(',')))
    
print(l,itemgetter(1,2,3))