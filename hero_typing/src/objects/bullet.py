import pygame
from settings import HEIGHT, C_WHITE
from src.objects.explosion import Explosion


class Bullet():

    dest_y = HEIGHT-249
    delete = False

    def __init__(self, screen, game_loop,  x) -> None:
        self.screen = screen
        self.game_loop = game_loop
        self.dest_x = x+40
        self.rect = pygame.Rect(self.dest_x, self.dest_y, 6, 10)

    def update(self):
        self.rect.y -= 8
        for index, letter in enumerate(self.game_loop.letters):
            if pygame.Rect.colliderect(self.rect, letter.rect):
                letter.life_count -= 1
                self.game_loop.screen_shake = 9
                self.delete = True
                self.game_loop.combo += 1
                self.game_loop.explosions.append(
                    Explosion(self.screen, (letter.rect.x+40, letter.rect.y+40))
                )
                if letter.life_count <= 0:
                    self.game_loop.letters.pop(index)
                    self.game_loop.points += self.game_loop.letter_value
                break
        
        if self.rect.y <= 0:
            self.game_loop.combo=0
            self.game_loop.errors+=1
            self.delete = True

    def draw(self):
        pygame.draw.rect(self.screen, C_WHITE, self.rect, 4)
