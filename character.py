

class Character:

    def __init__(self):
        pass


class NPC:
    def __init__(self, location):
        self.location = location #do we need this?



class PC:
    def __init__(self, name, appearance, pronouns):
        self.name = name
        self.appearance = appearance
        self.pronouns = pronouns

    def move(self):