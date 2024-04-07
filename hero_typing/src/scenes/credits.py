import pygame
import random
from settings import C_BLACK
from src.objects.letter import LetterBox


class Credits():

    def __init__(self, screen, game_loop, fonts) -> None:
        self.screen = screen
        self.game_loop = game_loop
        self.fonts = fonts

    def handle_event(self, events):
        for event in events:
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    self.game_loop.set_scene('menu')

    def update(self):
        for letter in self.game_loop.letters:
            letter.update()

    def draw(self):   
        self.screen.fill(C_BLACK)
        for letter in self.game_loop.letters:       
            letter.draw()