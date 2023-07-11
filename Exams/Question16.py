def check_password(password):
    if len(password) < 6 or len(password) > 12:
        return False
    lowercase = False
    uppercase = False
    number = False
    special_char = False

    for x in password:
        if x.islower():
            lowercase = True
        
        elif x.isupper():
            uppercase = True
        
        elif x.isdigit():
            number = True
        
        elif x in "$#@":
            special_char = True

    return lowercase and uppercase and number and special_char

def check_passwords(passwords):
    user_passwords = []
    for password in passwords:
        if check_password(password):
            user_passwords.append(password)
    return user_passwords

passwords = input("Enter comma-separated passwords: ").split(',')
n = check_passwords(passwords)
output = ",".join(n)
print(output)