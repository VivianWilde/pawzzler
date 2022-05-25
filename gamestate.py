import locations
from locations import Location
from character import Character, PC, NPC, Creature

view_width = 45
view_height = 32
WANDERING_WIDTH = 100
WANDERING_HEIGHT = 100
start_x = 5
start_y = 5
class Gamestate:

    def __init__(self, protag, wandering_map, start_map, gui): #gamestate stores world and current map
        self.protag = protag
        self.wandering_map = wandering_map #make new map magic
        self.wandering_map.add(start_map, 5, 5)#the numbers are the coordinates of the connection from start_map to wandering_map
        self.wandering_map.add_character(start_x, start_y)
        self.current_map = start_map
        self.gui = gui

    @staticmethod
    def new_game(gui):
        name, appearance, pronouns = gui.get_character_details()
        wandering_map = Location(WANDERING_WIDTH, WANDERING_HEIGHT, "grass")
        protag = PC(name, appearance, pronouns)
        start_map = Location(view_width,view_height, "floor")
        gamestate = Gamestate(protag, wandering_map, start_map, gui)
        return gamestate


    def initialize_game_from_file(self, file, level=0):
        cat_dialogue = 
        cat = Creature("Cat image", dialogue=)
        self.wandering_map.add(cat)

    def initialize_game_testing(self, level=0):


    def is_movable_cell(self, newpos):#this is relative newpos


    def update_character_pos(self, newpos):


    def get_command(self):
        self.gui.get_command


