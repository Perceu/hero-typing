import pygame
import random
from settings import C_WHITE, C_YELLOW, C_RED, WIDTH


x_positions = [i for i in range(250, WIDTH-400, 50)]

class LetterBox():
    letter = None
    x = 0
    y = 0
    vel = 1
    def __init__(self, screen, letter, font) -> None:
        self.screen = screen
        self.letter = letter
        self.font = font
        self.y = random.randint(-50, -2)
        self.x = random.choice(x_positions)

    def draw(self):
        if self.vel > 0 and self.vel < 2:
            pygame.draw.circle(self.screen, C_WHITE, (self.x+8, self.y+8), 24, 1)
        elif self.vel > 1 and self.vel < 3:
            pygame.draw.circle(self.screen, C_YELLOW, (self.x+8, self.y+8), 24, 1)
        else:
            pygame.draw.circle(self.screen, C_RED, (self.x+8, self.y+8), 24, 1)

        img = self.font.render(chr(self.letter).upper(), True, C_WHITE)
        self.screen.blit(img, (self.x, self.y))
    
    def update(self):
        self.y += self.vel
