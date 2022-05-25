import pygame
import os

WIDTH, HEIGHT = 1440, 1024
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Wandering Screen")

FPS = 60

HOMEBASE_IMAGE = pygame.image.load(os.path.join('pawzzler_GUI/Assets', 'Sketch_homebase.png'))
HOMEBASE = pygame.transform.scale(HOMEBASE_IMAGE, (300, 300))

CHARACTER_IMAGE = pygame.image.load(os.path.join('pawzzler_GUI/Assets', 'spaceship_yellow.png')) # replace with actual character graphic
CHARACTER_WIDTH, CHARACTER_HEIGHT = 110, 80
CHARACTER = pygame.transform.rotate(pygame.transform.scale(CHARACTER_IMAGE, (CHARACTER_WIDTH, CHARACTER_HEIGHT)), 90)
CHARACTER_VEL = 5

GREEN_GRASS = (99,205,110)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

def draw_welcome(): 
    return

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
        character.x -= CHARACTER_VEL # pass to backend to check if this is a legalmove. move if it is legal
    if keys_pressed[pygame.K_RIGHT]:  # right
        character.x += CHARACTER_VEL
    if keys_pressed[pygame.K_UP]:  # up
        character.y -= CHARACTER_VEL
    if keys_pressed[pygame.K_DOWN]:  # down
        character.y += CHARACTER_VEL

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
        character_moves(keys_pressed, character)
        draw_wandering(character)
    pygame.quit()

if __name__ == "__main__":
    initialize()
