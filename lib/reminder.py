
class Reminder:
    def __init__(self, name):
        self.name = name
        self.task = None

    def remind_me_to(self, task):
        self.task = task

    def remind(self):
    # Adapted to fail if there is no reminder set, with error message
        if self.task is None:
            raise Exception("No reminder set!")
        return f"{self.task}, {self.name}!"