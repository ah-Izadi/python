# class Text(dict):
#     def duplicate(self):
#         print(self + self)
    
    
# tmpstr = Text("python")


# tmpstr.duplicate()

class point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __eq__(self,other):
        return self.x == other.x and self.y == other.y
    
X = point(10,20)
Y = point(10,20)

print(id(X))
print(id(Y))
print(X==Y)




#named tuple
from collections import namedtuple
Point = namedtuple("Point","x,y")
point1 = Point(2,4)

print(point1.x == 4)