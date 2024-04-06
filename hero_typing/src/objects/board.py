import pygame
from settings import WIDTH, HEIGHT, C_GREY, C_RED, C_WHITE

class Board():

    def __init__(self, screen, game_loop) -> None:
        self.screen = screen
        self.game_loop = game_loop

    def draw(self):
        cenario_1 = pygame.Rect(298, 48, WIDTH-596, HEIGHT-246)
        cenario_2 = pygame.Rect(300, 50, WIDTH-600, HEIGHT-250)
        cenario_3 = pygame.Rect(302, 52, WIDTH-604, HEIGHT-254)

        if self.game_loop.damage > 0:
            self.game_loop.damage -= 1
            pygame.draw.rect(self.screen, C_GREY, cenario_1, 2)
            pygame.draw.rect(self.screen, C_RED, cenario_2, 2)
            pygame.draw.rect(self.screen, C_GREY, cenario_3, 2)
        else:
            pygame.draw.rect(self.screen, C_GREY, cenario_1, 2)
            pygame.draw.rect(self.screen, C_WHITE, cenario_2, 2)
            pygame.draw.rect(self.screen, C_GREY, cenario_3, 2)
