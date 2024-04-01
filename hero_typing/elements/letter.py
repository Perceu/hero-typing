import random
from settings import C_WHITE


x_positions = [110+(i*17) for i in range(30)]
y_positions = [(-17*i)-1 for i in range(10)]

class LetterBox():
    letter = None
    x = 0
    y = 0
    vel = 1
    def __init__(self, screen, letter, font, vel=1) -> None:
        self.screen = screen
        self.letter = letter
        self.font = font
        self.vel = vel
        self.y = random.choice(y_positions)
        self.x = random.choice(x_positions)

    def draw(self):
        img = self.font.render(chr(self.letter).upper(), True, C_WHITE)
        self.screen.blit(img, (self.x, self.y))
    
    def update(self):
        self.y += self.vel
