import pygame
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
        pass

    def draw(self):
        self.screen.fill(C_BLACK)
        letter3 = LetterBox(self.screen, self.game_loop, self.fonts, 110, life_count=3)
        letter3.rect.x = 200
        letter3.rect.y = 200
        letter3.draw()
        
        letter2 = LetterBox(self.screen, self.game_loop, self.fonts, 110, life_count=2)
        letter2.rect.x = 400
        letter2.rect.y = 400
        letter2.draw()