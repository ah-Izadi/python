class cmp:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
    def __cmp__(num1,num2):
        if num1 == num2:
            return 0
        elif num1 < num2:
            return -1
        else:
            return 1
p1 = cmp(2,4)
print(p1)