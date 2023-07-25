from lib.check_codeword import *

# def test_check_codeword_returns_correct_code():
#     if codeword == "horse":
#         return "Correct! Come in."
#     elif codeword[0] == "h" and codeword[-1] == "e":
#         return "Close, but nope."
#     else:
#         return "WRONG!"    

'''
If the codeword is correct
Return "Correct! Come in."
'''
def test_check_codeword_correct():
    result = check_codeword("horse")
    assert result == "Correct! Come in."

'''
If the codeword is incorrect
Return "WRONG!"
'''
def test_check_codeword_incorrect():
    result = check_codeword("mouse")
    assert result == "WRONG!"

'''
If codeword is almost correct 
return "Close, but nope."
'''
def test_check_codeword_right_first_and_last_letter():
    result = check_codeword("house")
    assert result == "Close, but nope."
