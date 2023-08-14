# # import time module
# import time
 
# # create sample code for testing
# for j in range(100, 5501, 100):
#     # store iteration start timestamp
#     start = time.time()
#     a = 0
#     for i in range(j):
#         a += (i**100)
#     # store iteration end timestamp
#     end = time.time()
 
#     # show time of execution per iteration
#     print(f"Iteration: {j}\tTime taken: {(end-start)*10**3:.03f}ms")
















import timeit
import math

start = timeit.default_timer()

#Your statements here

stop = timeit.default_timer()

print('Time: ', stop , start) 




































# import time
# import math
# while True:
#     start = time.time()
#     user_input = input('enter topping: ').upper()
#     if user_input == 'QUIT':
#         end = time.time()
#         print(f'You were in the loop for {(end-start)*10} milis')
#         # print((end-start)*10**3)
#         break
#     print(f'I add {user_input.title()} to your pizza :)')

# print(start)
# print(end)