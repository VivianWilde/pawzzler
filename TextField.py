import pygame


class TextField:
    def __init__(self, x, y, font, passive_color, active_color, text_color):
        self.user_text = ''
        self.x = x
        self.y = y
        self.font = font
        self.active = False
        self.passive_color = passive_color
        self.active_color = active_color
        self.color = passive_color
        self.text_color = text_color
        self.rect = pygame.Rect(x, y, 280, 64)

    def draw_text_field(self, WIN):
        run = True
        clock = pygame.time.Clock()
        while run:
            clock.tick(WIN.FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                pos = pygame.mouse.get_pos()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.rect.collidepoint(pos):
                        self.active = True
                    else:
                        self.active = False

                if self.active:
                    self.color = self.active_color
                    if event.key == pygame.K_BACKSPACE:
                        self.user_text = self.user_text[:-1]
                    else:
                        self.user_text += event.unicode
                else:
                    self.color = self.passive_color

            text_surface = self.font.render(self.user_text, False, self.text_color)
            pygame.draw.rect(WIN, self.color, self.rect, 2)
            WIN.blit(text_surface, (self.x + 5, self.y + 5))
            self.rect.w = max(140, text_surface.get_width() + 10)

