nums = list(range(1,21))
EvenNums = filter(lambda x: x % 2 == 0, nums)
print(list(EvenNums))