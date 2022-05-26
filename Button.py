import pygame

class Button():
    def __init__(self, x, y, image, scale):
        self.x = x
        self.y = y
        self.image = pygame.transform.scale(image, (image.get_width() * scale, image.get_height() * scale))
        self.rect = pygame.Rect(x, y, image.get_width() * scale, image.get_height() * scale)
        # self.clicked = False

    def draw_button(self, WIN):
        WIN.blit(self.image, (self.x, self.y))
        if self.click():
            return True
    
    def click(self):
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            # print('hover')
            if pygame.mouse.get_pressed()[0] == 1:
                return True
                # print('clicked')
                # self.clicked = True
