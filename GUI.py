import pygame
import os
# from gamestate import gamestate
from Button import Button

WIDTH, HEIGHT = 1440, 1024
GRIDWIDTH, GRIDHEIGHT = 32, 32
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pawzzler")

FPS = 60

NEWGAME_BIMAGE = pygame.image.load(os.path.join('Assets', 'new_game_button.png'))

HOMEBASE_IMAGE = pygame.image.load(os.path.join('Assets', 'Sketch_homebase.png'))
HOMEBASE = pygame.transform.scale(HOMEBASE_IMAGE, (300, 300))

CHARACTER_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_yellow.png')) # replace with actual character graphic
CHARACTER_WIDTH, CHARACTER_HEIGHT = 110, 80
CHARACTER = pygame.transform.rotate(pygame.transform.scale(CHARACTER_IMAGE, (CHARACTER_WIDTH, CHARACTER_HEIGHT)), 90)
CHARACTER_VEL = 5

WELCOME_COLOR = (99,205,110)
STARTING_COLOR = (99,205,110)
BUTTON_COLOR = (255, 255, 0)
GREEN_GRASS = (99,205,110)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

def draw_welcome(): 
    WIN.fill(STARTING_COLOR)
    pygame.font.init() 
    my_font = pygame.font.SysFont('Comic Sans MS', 30)
    title = my_font.render('Pawzzler!', False, BLACK)
    WIN.blit(title, (WIDTH/2, HEIGHT/4))

    # button in bottom third of the screen
    newgame_button = Button(WIDTH/2 - 250, HEIGHT/3, NEWGAME_BIMAGE, 0.5)
    draw_button(newgame_button)
    """
    pygame.draw.rect(WIN, BUTTON_COLOR, pygame.rect(WIDTH/2, 2*HEIGHT/3, 140, 40))
    new_game_text = my_font.render('New Game', False, BLACK)
    WIN.blit(new_game_text, (WIDTH/2, 2*HEIGHT/3))

    #if the mouse is clicked on the button, start new game
    if WIDTH/2 <= mouse[0] <= width/ 2+140 and height/2 <= mouse[1] <= height/2+40:
        pygame.quit()

    """

    pygame.display.update()



def draw_wandering(character):
    WIN.fill(GREEN_GRASS)
    WIN.blit(HOMEBASE, (WIDTH/2, HEIGHT/2))
    WIN.blit(CHARACTER, (character.x, character.y))
    pygame.display.update()

    """
    WIN.blit(CHARACTER, (yellow.x, yellow.y))
    WIN.blit(RED_SPACESHIP, (red.x, red.y))
    pygame.display.update()
    for bullet in red_bullets:
        pygame.draw.rect(WIN, RED, bullet)

    for bullet in yellow_bullets:
        pygame.draw.rect(WIN, YELLOW, bullet)
    """

def character_moves(keys_pressed, character):
    if keys_pressed[pygame.K_LEFT]:  # left
        try_move(-1, 0, character)
        # character.x -= CHARACTER_VEL # pass to backend to check if this is a legalmove. move if it is legal
    if keys_pressed[pygame.K_RIGHT]:  # right
        try_move(1, 0, character)
        # character.x += CHARACTER_VEL
    if keys_pressed[pygame.K_UP]:  # up
        try_move(0, -1, character)
        # character.y -= CHARACTER_VEL
    if keys_pressed[pygame.K_DOWN]:  # down
        try_move(0, 1, character)
        # character.y += CHARACTER_VEL

def try_move(xc, yc, character):
    gridxy = convert_pixels_to_grid(character.x + xc, + character.y + yc)
    if gamestate.is_movable_cell(gridxy):
        gamestate.update_character_pos(gridxy)
        character.x += CHARACTER_VEL * xc
        character.y += CHARACTER_VEL * yc

    
def convert_pixels_to_grid(x, y):
    return (x // GRIDWIDTH, y // GRIDHEIGHT)
    """
    gridx = x // GRIDWIDTH
    gridy = y // GRIDHEIGHT
    return (gridx, gridy)
    """

def draw_button(button):
    WIN.blit(button.image, (button.x, button.y))

def initialize():
    character = pygame.Rect(WIDTH/2, HEIGHT/2, CHARACTER_WIDTH, CHARACTER_HEIGHT)

    run = True
    clock = pygame.time.Clock()
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        keys_pressed = pygame.key.get_pressed()
        draw_welcome()
        """
        character_moves(keys_pressed, character)
        draw_wandering(character)
        """
    pygame.quit()

if __name__ == "__main__":
    initialize()
