import pytest 
from lib.password_checker import *

'''
Happy case: if password is empty
returns exception message
'''

def test_empty_password():
    password_checker = PasswordChecker()
    with pytest.raises(Exception) as e:
        password_checker.check(" ")
    error_message = str(e.value)
    error_message == "Password is empty!"

'''
If password length is incorrect
we see an error message
'''

def test_password_checker():
    password_checker = PasswordChecker()
    with pytest.raises(Exception) as e:
        password_checker.check("fruit")
    error_message = str(e.value)
    assert error_message == "Password is invalid - length requirement not met"