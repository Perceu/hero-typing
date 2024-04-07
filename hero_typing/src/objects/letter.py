import pygame
import random
from settings import C_WHITE, WIDTH, C_YELLOW, C_RED


x_positions = [i for i in range(340, WIDTH-620, 80)]


class LetterBox():
    color = C_WHITE
    b_color = C_WHITE
    life_count = 1
    colide = False
    velocity = 1

    def __init__(self, screen, game_loop, fonts, letter):
        self.screen = screen
        self.game_loop = game_loop
        self.fonts = fonts
        self.letter = letter
        self.surface = self.get_surface()
        self.rect = self.surface.get_rect()
        self.rect.x = random.choice(x_positions)

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
        if self.life_count > 2:
            for i in range(1, self.life_count):
                pygame.draw.rect(self.surface, self.b_color, pygame.Rect(i+(i*8), i+(i*8), 80-(i*16), 80-(i*16)), 2)
        else:
            for i in range(1, self.life_count):
                pygame.draw.rect(self.surface, self.b_color, pygame.Rect(i+(i*16), i+(i*16), 80-(i*32), 80-(i*32)), 2)

        self.surface.blit(img, (31,14))
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
        for letter in self.game_loop.letters:
            if letter.colide:
                continue
            if id(letter) == id(self):
                continue
            if pygame.Rect.colliderect(self.rect, letter.rect) == True:
                self.colide = True
                self.moveRight(15)
        
        self.moveDown(self.velocity)
    
    def draw(self):
        self.colide = False
        self.screen.blit(
            self.get_surface(), (self.rect.x, self.rect.y)
        )
