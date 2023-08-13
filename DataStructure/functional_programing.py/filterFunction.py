# filter()
ages = [12,14,20,30]

def Filter_age(age):
    if age > 18:
        return True
    
print(list(filter(Filter_age,ages)))