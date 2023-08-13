# class browser_session:
#     def __init__(self,User_input):
#         self.input = User_input
#         x = [0,1,2,3,4,5,6,7,8,9,10]
    
#     def back_data(self):
#         print(x[x]-1)



browser_session = []

browser_session.append(1)
browser_session.append(2)
browser_session.append(3)
print(browser_session)

last_item = browser_session.pop()
print(last_item)

print(browser_session[-1])
print(browser_session)

if not browser_session:
    print("browser sessions are empty")