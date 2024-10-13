import pygame
import random
from settings import C_WHITE, WIDTH, C_YELLOW, C_RED, C_PURPLE


x_positions = [i for i in range(340, WIDTH-620, 80)]


class LetterBox():
    color = C_WHITE
    life_count = 1
    points = 1
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

        if self.game_loop.level > 1 and self.game_loop.level < 3:
            self.velocity = random.randint(1, 2)
            if self.velocity == 2:
                self.color = C_YELLOW

        if self.game_loop.level > 3 and self.game_loop.level < 6:
            self.velocity = random.randint(1, 2)
            if self.velocity == 2:
                self.color = C_YELLOW
            if self.velocity == 3:
                self.color = C_RED

        if self.game_loop.level > 6 and self.game_loop.level < 9:
            self.velocity = random.randint(1, 3)
            self.life_count = random.randint(1, 2)
            if self.velocity == 2:
                self.color = C_YELLOW
            if self.velocity == 3:
                self.color = C_RED

        if self.game_loop.level > 9:
            self.life_count = random.randint(1, 3)
            self.velocity = random.randint(1, 4)
            if self.velocity == 2:
                self.color = C_YELLOW
            if self.velocity == 3:
                self.color = C_RED
            if self.velocity == 4:
                self.color = C_PURPLE

    def get_surface(self):
        self.surface = pygame.Surface((80,80), pygame.SRCALPHA)
        img = self.fonts['font_size_2'].render(self.letter.upper(), True, self.color)
        if self.life_count > 1:
            for i in range(1, self.life_count):
                pygame.draw.line(self.surface, self.color, (0 , 65+(i*3)), (80, 65+(i*3)), 1)

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
                self.moveRight(5)

        if self.velocity > 2:
            vel = random.randint(0, self.velocity)
            if vel:
                self.moveDown(vel)
            else:
                if random.randint(0,1):
                    self.moveLeft(2)
                if random.randint(0,1):
                    self.moveRight(2)
        else:
            self.moveDown(self.velocity)

    def draw(self):
        self.colide = False
        self.screen.blit(
            self.get_surface(), (self.rect.x, self.rect.y)
        )
