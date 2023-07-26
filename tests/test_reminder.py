import pytest
from lib.reminder import *

def test_reminder_to_do_a_useful_task():
    reminder = Reminder("Albert")
    reminder.remind_me_to("Proofread your paper")
    result = reminder.remind()
    assert result == "Proofread your paper, Albert!"

def test_raises_an_error_when_no_task_is_set():
    reminder = Reminder("Bettie")
    with pytest.raises(Exception) as err:
        reminder.remind()
    error_message = str(err.value)
    assert error_message == "No reminder set!"