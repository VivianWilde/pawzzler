import pygame, sys
# from tictactoe import *

pygame.init()

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600

LINE_COLOR = (129, 173, 200)
LINE_WIDTH = 15


screen = pygame.display.set_mode( (WINDOW_WIDTH, WINDOW_HEIGHT) )
pygame.display.set_caption('tic tac toe')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    pygame.display.update()

def draw_line():
    pygame.draw.line(screen, LINE_COLOR, (0,200), (600, 200), LINE_WIDTH)



# Board

BOARD_ROWS = 3
BOARD_COLS = 3

SQUARE_SIZE = 200
CIRCLE_RADIUS = 60
OFFSET = 55


