class rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width
        if self.width > self.length:
            print("The width cannot be greater than the length!!!")
            quit()
        
    def area(self):
        return self.length*self.width
    
    def primeter(self):
        return (self.length+self.width)*2

Rectangle = rectangle(int(input("please enter the length : ")),int(input("please enter the width : ")))
print(Rectangle.area())
print(Rectangle.primeter())