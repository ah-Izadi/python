class Check_Password:
    def __init__(self):
        pass
        
    def first_check_Password(self,r):
        if len(r) < 6 or len(r) > 12:
            return False
        lowercase = False
        uppercase = False
        number = False
        special_char = False

        for x in r:
            if x.islower():
                lowercase = True
            
            elif x.isupper():
                uppercase = True
            
            elif x.isdigit():
                number = True
            
            elif x in "$#@":
                special_char = True
            elif x in "!%^^&*":
                special_char = False

        return lowercase and uppercase and number and special_char

    def second_check_password(self,z):
        user_passwords = []
        for y in z:
            if self.first_check_Password(y):
                user_passwords.append(y)
        return user_passwords
        assert self.second_check_password("ABd1234@1,a F1#,2w3E*,2We3345") == ['ABd1234@1']