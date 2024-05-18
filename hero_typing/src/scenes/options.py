import pygame
from settings import C_BLACK, C_WHITE, C_GREEN


class Options():

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
        img_white = self.fonts["font_size_2"].render("Desenvolvido por", True, C_WHITE)
        self.screen.blit(img_white, (500, (80+40)))
        img_white = self.fonts["font_size_2"].render("Perceu G Bertoletti", True, C_GREEN)
        self.screen.blit(img_white, (500, (80+90)))