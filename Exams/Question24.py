# numsList = [1,2,3,4,5,6,7,8,9,10]
# def Filter_nums(number):
#     if number % 2 == 0:
#         return True

# evenNums = list(filter(Filter_nums,numsList))

# def Maping(input):
#     return input**2

# x = map(Maping,evenNums)
# print(list(x))

#best way
print(list(map(lambda x : x**2,filter(lambda a : a%2 == 0 , [1,2,3,4,5,6,7,8,9,10]))))