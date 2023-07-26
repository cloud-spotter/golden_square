from lib.reminder import *

def test_reminder_to_do_a_useful_task():
    reminder = Reminder("Albert")
    reminder.remind_me_to("Proofread your paper")
    result = reminder.remind()
    assert result == "Proofread your paper, Albert!"