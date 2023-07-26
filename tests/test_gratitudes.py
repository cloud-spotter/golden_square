from lib.gratitudes import *

def test_gratitudes_starts_as_formatted_empty_list():
    gratitudes = Gratitudes()
    assert gratitudes.format() == "Be grateful for: "

def test_gratitudes_adds_string_to_list():
    gratitudes = Gratitudes()
    gratitudes.add("friends")
    assert gratitudes.format() == "Be grateful for: friends"

def test_gratitudes_adds_and_concatenates_strings_to_list():
    gratitudes = Gratitudes()
    gratitudes.add("friends")
    gratitudes.add("opportunities to learn new skills")
    assert gratitudes.format() == "Be grateful for: friends, opportunities to learn new skills"
