def divide_by_zero():
    try:
        result = 5 / 0
    except ZeroDivisionError:
        print("Division by zero!!!!!")

divide_by_zero()