def unpacking_list(collection):
        for x in collection:
            print(x)

x = list(range(10))
listname = ["ali", "babak"]
# y = *listname

thisDict = {'ali':36,'hossein':12,'asghar':19}
secDict = {'ali':69,'hossein':543,'asghar':56}
combin = {**thisDict, **secDict}
print(combin)