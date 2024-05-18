import pygame
from settings import C_YELLOW, WIDTH, C_BLACK

class Points(): 

    def __init__(self, screen, game_loop, fonts) -> None:
        self.screen = screen
        self.game_loop = game_loop
        self.fonts = fonts

    def draw(self):
        point = self.game_loop.points
        rect = pygame.Rect(0,0, WIDTH, 50)
        img = self.fonts['font_size_2'].render(
            str(point).zfill(5), True, C_YELLOW
        )
        final_w = (WIDTH/2) - (img.get_width()/2)
        pygame.draw.rect(self.screen, C_BLACK, rect)
        self.screen.blit(img, (final_w, 5))