import pygame
from settings import HEIGHT, C_WHITE, C_RED, C_YELLOW
from src.objects.explosion import Explosion
from random import randint

class Bullet():

    dest_y = HEIGHT-110
    delete = False

    def __init__(self, screen, game_loop,  x, sounds) -> None:
        self.screen = screen
        self.sounds = sounds
        self.game_loop = game_loop
        self.dest_x = x+40
        self.rect = pygame.Rect(self.dest_x, self.dest_y, 6, 10)

    def update(self):
        self.rect.y -= 6
        for index, letter in enumerate(self.game_loop.letters):
            if pygame.Rect.colliderect(self.rect, letter.rect):
                letter.life_count -= 1
                self.game_loop.screen_shake = 9
                self.delete = True
                self.game_loop.combo += 1
                self.game_loop.explosions.append(
                    Explosion(self.screen, (letter.rect.x+40, letter.rect.y+40))
                )
                pygame.mixer.Sound.play(self.sounds[1])
                if letter.life_count <= 0:
                    self.game_loop.letters.pop(index)
                    self.game_loop.points += letter.points
                break

        if self.rect.y <= 0:
            self.game_loop.combo=0
            self.game_loop.errors+=1
            self.delete = True

    def draw(self):
        pygame.draw.rect(self.screen, C_WHITE, self.rect, 4)

class Bullet2():

    dest_y = HEIGHT-110
    delete = False

    def __init__(self, screen, game_loop,  x, sounds) -> None:
        self.screen = screen
        self.sounds = sounds
        self.game_loop = game_loop
        self.dest_x = x+40
        self.dest_x_o = x+40
        self.rect = pygame.Rect(self.dest_x, self.dest_y, 6, 12)

    def update(self):
        self.rect.y -= 10
        for index, letter in enumerate(self.game_loop.letters):
            if pygame.Rect.colliderect(self.rect, letter.rect):
                letter.life_count -= 1
                self.game_loop.screen_shake = 9
                self.delete = True
                self.game_loop.combo += 1
                self.game_loop.explosions.append(
                    Explosion(self.screen, (letter.rect.x+40, letter.rect.y+40))
                )
                pygame.mixer.Sound.play(self.sounds[1])
                if letter.life_count <= 0:
                    self.game_loop.letters.pop(index)
                    self.game_loop.points += letter.points
                break

        if self.rect.y <= 0:
            self.game_loop.combo=0
            self.game_loop.errors+=1
            self.delete = True

    def draw(self):
        self.rect.height = randint(8,12)
        self.rect.x = self.dest_x_o + randint(-2,2)
        pygame.draw.rect(self.screen, C_YELLOW, self.rect)

class Bullet3():

    dest_y = HEIGHT-110
    delete = False

    def __init__(self, screen, game_loop,  x, sounds) -> None:
        self.screen = screen
        self.sounds = sounds
        self.game_loop = game_loop
        self.dest_x = x+40
        self.rect = pygame.Rect(self.dest_x, self.dest_y, 6, 12)
        self.rect2 = pygame.Rect(self.dest_x, self.dest_y+15, 6, 6)

    def update(self):
        self.rect.y -= 12
        self.rect2.y -= 12
        for index, letter in enumerate(self.game_loop.letters):
            if pygame.Rect.colliderect(self.rect, letter.rect):
                letter.life_count -= 1
                self.game_loop.screen_shake = 9
                self.delete = True
                self.game_loop.combo += 1
                self.game_loop.explosions.append(
                    Explosion(self.screen, (letter.rect.x+40, letter.rect.y+40))
                )
                pygame.mixer.Sound.play(self.sounds[1])
                if letter.life_count <= 0:
                    self.game_loop.letters.pop(index)
                    self.game_loop.points += letter.points
                break

        if self.rect.y <= 0:
            self.game_loop.combo=0
            self.game_loop.errors+=1
            self.delete = True

    def draw(self):
        self.rect.height = randint(8,12)
        pygame.draw.rect(self.screen, C_RED, self.rect)
        pygame.draw.rect(self.screen, C_YELLOW, self.rect2)
