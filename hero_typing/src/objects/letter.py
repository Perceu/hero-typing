import pygame
import random
from settings import C_WHITE, WIDTH, C_YELLOW, C_RED


x_positions = [i for i in range(308, WIDTH-608, 80)]


class LetterBox():
    color = C_WHITE
    b_color = C_WHITE
    life_count = 1
    def __init__(self, screen, game_loop, fonts, letter, life_count=1, velocity=1):
        self.screen = screen
        self.game_loop = game_loop
        self.fonts = fonts
        self.letter = letter
        self.surface = self.get_surface()
        self.rect = self.surface.get_rect()
        self.rect.x = random.choice(x_positions)
        self.velocity = velocity
        self.life_count = life_count

        if self.game_loop.level > 1:
            self.velocity = random.randint(1, self.game_loop.velocity)
            if self.velocity == 2:
                self.color = C_YELLOW
            if self.velocity > 2:
                self.color = C_RED
            if self.velocity > 3:
                self.b_color = C_RED
            self.life_count = random.randint(1, 3)

        if self.game_loop.level > 10:
            self.life_count = random.randint(2, 4)

    def get_surface(self):
        self.surface = pygame.Surface((80,80), pygame.SRCALPHA)
        img = self.fonts['font_size_2'].render(chr(self.letter).upper(), True, self.color)
        if self.life_count > 1:
            print('=====')
            for i in range(self.life_count-1):
                pygame.draw.rect(self.surface, self.b_color, pygame.Rect(i+(i*8), i+(i*8), 80-(i*16), 80-(i*16)), 2)

        self.surface.blit(img, (30,9))
        return self.surface

    def moveRight(self, pixels):
        self.rect.x += pixels

    def moveLeft(self, pixels):
        self.rect.x -= pixels

    def moveUp(self, pixels):
        self.rect.y -= pixels

    def moveDown(self, pixels):
        self.rect.y += pixels

    def update(self) -> None:
        self.moveDown(self.velocity)
    
    def draw(self):
        self.screen.blit(
            self.get_surface(), (self.rect.x, self.rect.y)
        )

