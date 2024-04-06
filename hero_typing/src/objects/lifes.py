import pygame
from settings import C_GREEN


class Lifes(): 

    def __init__(self, screen, game_loop) -> None:
        self.game_loop = game_loop
        self.screen = screen

    def substract_lifes(self, damage=1):
        self.game_loop.lifes -= damage

    def draw(self):
        for i in range(1, self.game_loop.lifes+1):
            rect_live = pygame.Rect(25*i, 50, 20, 20)
            pygame.draw.rect(self.screen, C_GREEN, rect_live)