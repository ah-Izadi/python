from abc import ABC, abstractmethod

class UIInterface(ABC):
    @abstractmethod
    def draw():
        pass
    
class TextBox:
    def draw(self):
        print("Draw TextBox")
    

class DropDown:
    def draw(self):
        print("Draw DropDown")


def draw(controls):
    for control in controls:
        print(control.draw())
    
txtBox = TextBox()
dropDown = DropDown()
# print(isinstance(txtBox,UIInterface))

draw([txtBox,dropDown])