# 4 Pillars of OOP
# Encapsulation - Enclosing attributes and methods inside a capsule code
class PlayerCharacter:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"My name is {self.name}"
