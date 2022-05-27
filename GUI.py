import pygame
import os
from gamestate import Gamestate
from Button import Button
from TextField import TextField

pygame.font.init()
basic_font = pygame.font.SysFont('Comic Sans MS', 30)

WELCOME_COLOR = (109, 192, 238)
CHARSCREEN_COLOR = (109, 192, 238)
GREEN_GRASS = (99, 205, 110)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

character_image_options = os.listdir('Assets/character_image_options')


class GUI():
    WIDTH, HEIGHT = 1440, 1024
    GRIDWIDTH, GRIDHEIGHT = 32, 32
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Pawzzler")

    FPS = 60

    started_newgame = False
    gamestate = None
    NEWGAME_BIMAGE = pygame.image.load(os.path.join('Assets', 'new_game_button.png'))

    HOMEBASE_IMAGE = pygame.image.load(os.path.join('Assets', 'Sketch_homebase.png'))
    HOMEBASE = pygame.transform.scale(HOMEBASE_IMAGE, (300, 300))

    CHARACTER_NAME = ''
    CHARACTER_PRONOUNS = ''
    CHARACTER_IMAGE = pygame.image.load(os.path.join('Assets/character_image_options', character_image_options[0]))
    CHARACTER_WIDTH, CHARACTER_HEIGHT = CHARACTER_IMAGE.get_width(), CHARACTER_IMAGE.get_height()
    """
    CHARACTER_IMAGE = pygame.image.load(
        os.path.join('Assets', 'spaceship_yellow.png'))  # replace with actual character graphic
    CHARACTER_WIDTH, CHARACTER_HEIGHT = 110, 80
    CHARACTER = pygame.transform.rotate(pygame.transform.scale(CHARACTER_IMAGE, (CHARACTER_WIDTH, CHARACTER_HEIGHT)),
                                        90)
    """

    CHARACTER_VEL = 5

    def draw_welcome(self):
        self.WIN.fill(WELCOME_COLOR)
        title = basic_font.render('Pawzzler!', False, BLACK)
        self.WIN.blit(title, (self.WIDTH / 2, self.HEIGHT / 4))

        # button in bottom third of the screen
        newgame_button = Button(self.WIDTH / 2 - 250, self.HEIGHT / 3, self.NEWGAME_BIMAGE, 0.5)
        """
        WIN.blit(newgame_button.image, (newgame_button.x, newgame_button.y))
        if newgame_button.click():
            draw_choosechar()
        """
        if newgame_button.draw_button(self.WIN):
            # print('clicked')
            self.gamestate = Gamestate.new_game(self)
            started_newgame = True
            # self.draw_choosechar()
        pygame.display.update()

    def get_character_details(self):
        """
        call draw choose char screen
        user chooses character
        R name, appearance, pronouns
        """
        self.draw_choosechar()
        return self.NAME, self.CHARACTER_PRONOUNS, self.CHARACTER_IMAGE

    def draw_choosechar(self):
        self.WIN.fill(CHARSCREEN_COLOR)
        run = True
        clock = pygame.time.Clock()
        while run:
            clock.tick(self.FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            # keys_pressed = pygame.key.get_pressed()

            # set name
            username = TextField(120, 120, basic_font, WHITE, BLACK, BLACK)
            username.draw_text_field(self.WIN)
            self.CHARACTER_NAME = username.user_text

            # set pronouns
            userpronouns = TextField(120, 236, basic_font, WHITE, BLACK, BLACK)
            userpronouns.draw_text_field(self.WIN)
            self.CHARACTER_PRONOUNS = userpronouns.user_text

            # set appearance
            self.WIN.blit(self.CHARACTER_IMAGE, (970, 215))



        pygame.display.update()

    def draw_wandering(self, character):
        self.WIN.fill(GREEN_GRASS)
        self.WIN.blit(self.HOMEBASE, (self.WIDTH / 2, self.HEIGHT / 2))
        self.WIN.blit(self.CHARACTER, (character.x, character.y))
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

    def character_moves(self, keys_pressed, character):
        if keys_pressed[pygame.K_LEFT]:  # left
            self.try_move(-1, 0, character)
            # character.x -= CHARACTER_VEL # pass to backend to check if this is a legalmove. move if it is legal
        if keys_pressed[pygame.K_RIGHT]:  # right
            self.try_move(1, 0, character)
            # character.x += CHARACTER_VEL
        if keys_pressed[pygame.K_UP]:  # up
            self.try_move(0, -1, character)
            # character.y -= CHARACTER_VEL
        if keys_pressed[pygame.K_DOWN]:  # down
            self.try_move(0, 1, character)
            # character.y += CHARACTER_VEL

    def try_move(self, xc, yc, character):
        gridxy = self.convert_pixels_to_grid(character.x + xc, + character.y + yc)
        if self.gamestate.current_map.movable(gridxy):
            self.gamestate.current_map.update(gridxy)
            character.x += self.CHARACTER_VEL * xc
            character.y += self.CHARACTER_VEL * yc

    def convert_pixels_to_grid(self, x, y):
        return (x // self.GRIDWIDTH, y // self.GRIDHEIGHT)
        """
        gridx = x // GRIDWIDTH
        gridy = y // GRIDHEIGHT
        return (gridx, gridy)
        """

    def initialize(self):
        character = pygame.Rect(self.WIDTH / 2, self.HEIGHT / 2, self.CHARACTER_WIDTH, self.CHARACTER_HEIGHT)

        run = True
        clock = pygame.time.Clock()
        while run:
            clock.tick(self.FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            keys_pressed = pygame.key.get_pressed()
            self.draw_welcome()

            """
            while run and self.started_newgame == False:
                self.draw_welcome(character)
                if self.started_newgame:
                    break
        
            character_moves(keys_pressed, character)
            draw_wandering(character)
            """
        pygame.quit()
