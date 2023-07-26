from lib.string_builder import *

def test_string_builder_starts_as_empty_string():
    string_builder = StringBuilder()
    assert string_builder.output() == ""

# This test is covered in later test (add multiple strings)
# def test_string_builder_add_string():
#     string_builder = StringBuilder()
#     string_builder.add("sherbert")
#     assert string_builder.output() == "sherbert"

def test_string_builder_add_multiple_strings():
    string_builder = StringBuilder()
    string_builder.add("sherbert")
    string_builder.add(" lemons")
    assert string_builder.output() == "sherbert lemons"

# This test is covered by the next test (return size multiple strings)
# def test_string_builder_return_size_single_string_added():
#     string_builder = StringBuilder()
#     string_builder.add("sherbert lemons")
#     assert string_builder.size() == 15

def test_string_builder_return_size_multiple_strings_added():
    string_builder = StringBuilder()
    string_builder.add("sherbert lemons")
    string_builder.add(" are zingy")
    assert string_builder.size() == 25