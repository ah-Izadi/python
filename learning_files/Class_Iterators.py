class numclass:
    
    def __iter__(self):
        self.x = 0
        return self
    def __next__(self):
        if self.x < 21:
            a = self.x
            self.x += 1
            return a
        else:
            raise StopIteration
    
IterClass = numclass()
Iterator = iter(IterClass)

print(next(Iterator))
print(next(Iterator))
print(next(Iterator))
print(next(Iterator))
print(next(Iterator))
print(next(Iterator))
print(next(Iterator))
print(next(Iterator))
print(next(Iterator))
print(next(Iterator))
print(next(Iterator))
print(next(Iterator))
print(next(Iterator))
print(next(Iterator))
print(next(Iterator))
print(next(Iterator))
print(next(Iterator))
print(next(Iterator))
print(next(Iterator))
print(next(Iterator))
print(next(Iterator))