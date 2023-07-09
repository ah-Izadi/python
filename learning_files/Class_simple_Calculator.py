class Claculator:
    def __init__(self,firstNum,secondNum):
        self.x = firstNum
        self.y = secondNum
    def multiply(self):
        return(self.x*self.y)
    def division(self):
        return(self.x/self.y)
    def plus(self):
        return(self.x+self.y)
    def minus(self):
        return(self.x-self.y)

inputNum1 = int(input("please enter first number : "))
inputNum2 = int(input("please enter second number : "))

calc = Claculator(inputNum1,inputNum2)
print(calc.minus())