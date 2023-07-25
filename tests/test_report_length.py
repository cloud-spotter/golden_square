# def report_length(str):
#     length = len(str)
#     return f"This string was {length} characters long."

from lib.report_length import *

# Test for correct output
def test_report_length_correct():
    result = report_length("four")
    assert result == "This string was 4 characters long."

# Test for empty string
def test_report_length_empty_string():
    result = report_length("")
    assert result == "This string was 0 characters long."

# Test for string with multiple words
def test_report_length_empty_string():
    result = report_length("hello world")
    assert result == "This string was 11 characters long."