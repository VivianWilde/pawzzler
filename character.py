
class Character:
    def __init__(self, appearance):
        self.appearance = appearance
        self.map = None
        self.loc = None
        pass

    def move(self, x_dir, y_dir):
        self.location.move()

class NPC(Character, Interactable):
    def __init__(self, appearance, dialogue=None):
        super.__init__(appearance)
        self.dialogue = dialogue
        pass


class Creature(NPC):
    def __init__(self, appearance, dialogue):
        super().__init__(appearance, dialogue)

class PC(Character):
    def __init__(self, name, appearance, pronouns, start_map):
        super(PC, self).__init__(self, , appearance)
        self.name = name
        self.pronouns = pronouns
