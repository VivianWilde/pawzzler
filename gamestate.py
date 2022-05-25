import locations
from locations import Location
from character import Character, PC, NPC, Creature

view_width = 45
view_height = 32


class Gamestate:

    def __init__(self, protag, world=None, start_map=None, gui): #gamestate stores world and current map
        self.protag = protag
        self.world = world #make new map magic
        self.world.add(start_map, 5, 5)
        self.current_map = start_map
        self.gui = gui

    @staticmethod
    def new_game():
        name, appearance, pronouns = #magic(frontend)
        world = Location(32, 20, "grass")
        protag = PC(name, appearance, pronouns)
        protag.loc = locations.center(world)
        start_map = Location(32, 20, "floor")
        gui = GUI()
        gamestate = Gamestate(protag, world, start_map, gui)
        gamestate.initialize_game()
        return gamestate


    def initialize_game(self, file, level=0):
        cat_dialogue = 
        cat = Creature("Cat image", dialogue=)
        self.world.add(cat)

    def initialize_game_testing(self, level=0):


    def is_movable_cell(self, newpos):


    def update_character_pos(self, newpos):


    def get_command(self):
        self.gui.get_command


