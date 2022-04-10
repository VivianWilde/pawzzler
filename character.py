
class Character:
    def __init__(self, appearance, map, x, y):
        self.appearance = appearance
        self.map = map
        self.map.add(self, map, x, y)
        self.loc = (x, y)
        pass

    def move(self, x_dir, y_dir):
        self.location.move()

class NPC(Character, Interactable):
    def __init__(self, appearance, map, dialogue=None):
        super.__init__(appearance, map)
        self.dialogue = dialogue
        pass


class Creature(NPC):
    def __init__(self, appearance, map, dialogue):
        super().__init__(appearance, map, dialogue)

class PC(Character):
    def __init__(self, name, appearance, pronouns, start_map, x, y):
        super(PC, self).__init__(self, start_map, appearance, x, y)
        self.name = name
        self.pronouns = pronouns
