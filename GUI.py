import pygame
import os
from gamestate import Gamestate
from Button import Button

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
    CHARACTER_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_yellow.png')) # replace with actual character graphic
    CHARACTER_WIDTH, CHARACTER_HEIGHT = 110, 80
    CHARACTER = pygame.transform.rotate(pygame.transform.scale(CHARACTER_IMAGE, (CHARACTER_WIDTH, CHARACTER_HEIGHT)), 90)
    CHARACTER_VEL = 5

    WELCOME_COLOR = (99,205,110)
    STARTING_COLOR = (99,205,110)
    CHARSCREEN_COLOR = (99,205,110)
    GREEN_GRASS = (99,205,110)
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    YELLOW = (255, 255, 0)

    def draw_welcome(self, character): 
        self.WIN.fill(self.STARTING_COLOR)
        pygame.font.init() 
        my_font = pygame.font.SysFont('Comic Sans MS', 30)
        title = my_font.render('Pawzzler!', False, self.BLACK)
        self.WIN.blit(title, (self.WIDTH/2, self.HEIGHT/4))

        # button in bottom third of the screen
        newgame_button = Button(self.WIDTH/2 - 250, self.HEIGHT/3, self.NEWGAME_BIMAGE, 0.5)
        """
        WIN.blit(newgame_button.image, (newgame_button.x, newgame_button.y))
        if newgame_button.click():
            draw_choosechar()
        """
        if newgame_button.draw_button(self.WIN):
            # print('clicked')
            # self.gamestate = Gamestate.new_game(self)
            started_newgame = True
            # self.draw_choosechar()

        """
        pygame.draw.rect(WIN, BUTTON_COLOR, pygame.rect(WIDTH/2, 2*HEIGHT/3, 140, 40))
        new_game_text = my_font.render('New Game', False, BLACK)
        WIN.blit(new_game_text, (WIDTH/2, 2*HEIGHT/3))

        #if the mouse is clicked on the button, start new game
        if WIDTH/2 <= mouse[0] <= width/ 2+140 and height/2 <= mouse[1] <= height/2+40:
            pygame.quit()

        """

        pygame.display.update()

    def get_character_details(self):
        """
        user chooses character
        R name, appearance, pronouns
        """

    def draw_choosechar(self):
        self.WIN.fill(self.CHARSCREEN_COLOR)


        pygame.display.update()



    def draw_wandering(self, character):
        self.WIN.fill(self.GREEN_GRASS)
        self.WIN.blit(self.HOMEBASE, (self.WIDTH/2, self.HEIGHT/2))
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
        if self.gamestate.is_movable_cell(gridxy):
            self.gamestate.update_character_pos(gridxy)
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
        character = pygame.Rect(self.WIDTH/2, self.HEIGHT/2, self.CHARACTER_WIDTH, self.CHARACTER_HEIGHT)

        run = True
        clock = pygame.time.Clock()
        while run:
            clock.tick(self.FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            
            keys_pressed = pygame.key.get_pressed()
            while run and self.started_newgame == False:
                self.draw_welcome(character)
                if self.started_newgame:
                    break
            
            while run: 
                self.draw_choosechar()
            
            """
            character_moves(keys_pressed, character)
            draw_wandering(character)
            """
        pygame.quit()

