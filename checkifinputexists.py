# user_input = list(input().split(' 'or','))
# for x in user_input:
#     if x == ' ' or not x:
#         print('password hasn`t been entred')
#         quit()

# if user_input:
#     print("password is :",user_input)

import getopt
import sys
 
first =""
last =""
argv = sys.argv[1:]
try:
    options, args = getopt.getopt(argv, "f:l:",
                               ["ip =",
                                "port ="])
except:
    print("Error Message ")
 
for name, value in options:
    if name in ['-ip', '--first']:
        first = value
    elif name in ['-port', '--last']:
        last = value
 
print(first + " " + last)