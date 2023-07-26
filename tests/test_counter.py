from lib.counter import *

def test_counter_start_at_zero():
    counter = Counter()
    assert counter.report() == "Counted to 0 so far."

def test_counter_add_number():
    counter = Counter()
    counter.add(5)
    assert counter.report() == "Counted to 5 so far."

def test_counter_add_multiple_numbers():
    counter = Counter()
    counter.add(5)
    counter.add(6)
    assert counter.report() == "Counted to 11 so far."

def test_counter_add_negative_number():
    counter = Counter()
    counter.add(5)
    counter.add(-6)
    assert counter.report() == "Counted to -1 so far."