import pygame
from settings import C_RED


class Lifes(): 
    lifes = 0
    def __init__(self, screen, lifes) -> None:
        self.lifes = lifes
        self.screen = screen

    def substract_lifes(self):
        self.lifes -= 1

    def draw(self):
        for i in range(self.lifes):
            rect_live = pygame.Rect((i*10)+12, 65, 5, 10)
            pygame.draw.rect(self.screen, C_RED, rect_live)