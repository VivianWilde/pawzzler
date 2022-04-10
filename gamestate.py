import locations
from locations import Location
from character import Character, PC, NPC, Creature

class Gamestate:

    def __init__(self, protag, world=None, start_map=None):
        self.protag = protag
        self.world = world #make new map magic
        self.world.add(start_map, 5, 5)
        self.map = start_map

    @staticmethod
    def new_game():
        name, appearance, pronouns = #magic(frontend)
        world = Location(32, 20, "grass")
        protag = PC(name, appearance, pronouns)
        protag.loc = locations.center(world)
        start_map = Location(32, 20, "floor")
        gamestate = Gamestate(protag, world, start_map)
        gamestate.initialize_game()
        return gamestate


    def initialize_game_from_file(self, level=0):
        cat_dialogue = 
        cat = Creature("Cat image", dialogue=)
        self.world.add(cat)


