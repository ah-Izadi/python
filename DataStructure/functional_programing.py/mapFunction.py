"""
map()
"""

mainList = ['amir' ,'mmd' ,'hossein']
 
def show(name):
    print(f'hello {name}')
    
list(map(show,mainList))