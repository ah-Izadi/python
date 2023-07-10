class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def draw(self):
        print(f'point ({x},{y})')
    def __add__(self,y):
        return Point(self.x + self.y , other.x + other.y)
    def __str__(self):
        return f"({self.x},{self.y})"
    def __eq__(self,y):
        return self.x == y.x and y.y == self.y
    def __gt__(self,y):
        return self.x > y.x and self.y > y.y
point = Point(1,2)
other = Point(3,4)

print(point < other)