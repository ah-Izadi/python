class animal:
    def __init__(self):
        print("animal constructor")
        self.age = 1
    def eat(self):
        print("eat!")
        
class mamal(animal):
    def __init__(self):
        print("mamal constructor")
        self.height = 2
        super().__init__()
    def walk(self):
        print("walk!")

class fish():
    def __init__(self):
        # super().__init__(self)
        print("fish constructor")
    def swiming(self):
        print("Swim!")

x = mamal()
x.eat()
print(x.age)
# x.

# y = fish()
# y.eat()
# print(x.age)

print(isinstance(x,animal))
print(issubclass(fish,animal))