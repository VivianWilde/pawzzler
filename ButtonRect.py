import pygame

class ButtonRect():
    def __init__(self, x, y, text, text_color, width, height, passive_color, active_color, font):
        self.x = x
        self.y = y
        self.text = text
        self.text_color = text_color
        self.rect = pygame.Rect(x, y, width, height)
        self.passive_color = passive_color
        self.active_color = active_color # this is for more advanced version
        self.color = passive_color
        self.font = font

        # self.clicked = False

    def draw_button(self, WIN):
        text_surface = self.font.render(self.text, False, self.text_color)
        pygame.draw.rect(WIN, self.color, self.rect)
        WIN.blit(text_surface, (self.x + 5, self.y + 5))

        # return self.click()
        # """
        if self.click():
            return True 
        # """
    
    def click(self):
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                return True
