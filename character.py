class PC:
    def __init__(self, name, appearance, pronouns):
        self.name = name
        self.appearance = appearance
        self.pronouns = self.parse_pronouns(pronouns)
        self.inventory = []
    # TODO: All the rest, like handling appearances, etc.

    def parse_pronouns(self, pronouns):
        return pronouns.split("/")

    def add_to_inventory(self, item):
        self.inventory.append(item)
