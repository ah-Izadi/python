class Airplane:
    def __init__(self):
        pass
    
    def move(self):
        print("mAirplaneoooooooooove")
        
        
class Car:
    def __init__(self):
        pass
    
    def move(self):
        print("car moooooooooove")
    
class Vehicle(Airplane, Car):
    pass

v = Vehicle()
v.move()