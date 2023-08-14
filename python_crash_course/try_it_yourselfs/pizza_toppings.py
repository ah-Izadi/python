while True:
    topping = input('enter topping: ').upper()
    if topping == 'QUIT':
        break
    else:
        print(f'I add {topping.title()} topping to your pizza')
    