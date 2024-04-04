import pygame

class BaseScene:

    def __init__(self, game_loop, screen) -> None:
        self.screen = screen
        self.game_loop = game_loop