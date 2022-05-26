import locations
import stock_objects
from locations import Location
from character import PC


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
        stock_objects.main()
        wandering_map = stock_objects.from_info("Wandering screen", "Location")
        start_map = stock_objects.from_info("Homebase", "Location")
        protag = PC(name, appearance, pronouns)
        gamestate = Gamestate(protag, wandering_map, start_map, gui)
        return gamestate

    # def initialize_game_from_file(self, file, level=0):
    #     cat_dialogue =
    #     cat = Creature("Cat image", dialogue=)
    #     self.wandering_map.add(cat)

    def initialize_game_testing(self, level=0):
        pass


    def get_command(self):
        self.gui.get_command


