class PasswordChecker:
    def check(self, password):
        if len(password) >= 8:
            return True
        elif password == " ":
            raise Exception("Password is empty!")
        else:
            raise Exception("Password is invalid - length requirement not met")
    


# password_checker = PasswordChecker()
# print(password_checker.check("password"))
# print(password_checker.check("donkeys"))


