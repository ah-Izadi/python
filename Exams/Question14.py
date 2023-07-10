class Circle:
    def __init__(self,radius):
        self.area = radius*radius*3.14
        self.primeter = radius*2*3.14

circle = Circle(int(input("please enter radius : ")))
print(circle.area)
print(circle.primeter)