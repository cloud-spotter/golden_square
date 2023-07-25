from lib.greet import *

def test_greet_print_return_with_given_name():
    result = greet("Kim")
    assert result == "Hello, Kim!"