class Gratitudes:
    def __init__(self):
        self.gratitudes = []

    def add(self, gratitude):
        self.gratitudes.append(gratitude)

    def format(self):
        formatted = "Be grateful for: "
        formatted += ", ".join(self.gratitudes)
        return formatted
    
gratitudes = Gratitudes()
gratitudes.add("friends")
gratitudes.add("opportunities to learn new skills")
print(gratitudes.format())