import pytest
from lib.present import *

'''
Happy case: when you wrap an item 
You get it back when unwrapping
'''

def test_wrap_and_then_unwrap():
    present = Present()
    present.wrap(29)
    assert present.unwrap() == 29

'''
If we unwrap before wrapping
we get an error
'''

def test_unwrap_before_wrapping_fails():
    present = Present()
    with pytest.raises(Exception) as err:
        present.unwrap()
    error_message = str(err.value)
    assert error_message == "No contents have been wrapped." 

'''
If we try to wrap an already wrapped present
We get an error message
'''

def test_wrapping_aready_wrapped_throws_error():
    present = Present()
    present.wrap("orchid")
    with pytest.raises(Exception) as err:
        present.wrap("begonia") 
    message = str(err.value)
    assert message == "A contents has already been wrapped."

'''
If we try to wrap an already wrapped present, 
the first-wrappped value is unchanged
'''

def test_wrapping_already_wrapped_preserves_value():
    present = Present()
    present.wrap("orchid")
    with pytest.raises(Exception) as err:
        present.wrap("begonia") 
    message = str(err.value)
    assert present.unwrap() == "orchid"