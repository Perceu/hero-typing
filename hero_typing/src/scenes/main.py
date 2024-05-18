import pygame
import random
from settings import C_BLACK, WIDTH, HEIGHT
from src.scenes.enum_scene import EnumScenes
from src.objects.lifes import Lifes
from src.objects.explosion import Explosion
from src.objects.letter import LetterBox
from src.objects.points import Points
from src.objects.level import Level
from src.objects.board import Board
from src.objects.infobox import Infobox
from src.objects.bullet import Bullet, Bullet2, Bullet3


def get_valid_letter(game_loop, level_array):
    sort_letter = True
    temp_ord = random.choice(level_array)
    while sort_letter:
        match_letter = False
        for letter in game_loop.letters:
            if temp_ord == letter.letter:
                match_letter = True

        if not match_letter:
            sort_letter = False
            continue
        temp_ord = random.choice(level_array)

    return temp_ord


class MainGame():

    render_offset = [0,0]
    screen_shake = 0

    def __init__(self, screen, game_loop, fonts, sounds) -> None:
        self.screen = screen
        self.game_loop = game_loop
        self.fonts = fonts
        self.sounds = sounds
        self.life_bar = Lifes(screen, self.game_loop)
        self.points = Points(self.screen, self.game_loop, self.fonts)
        self.level = Level(self.screen, self.game_loop, self.fonts)
        self.board = Board(self.screen, self.game_loop)
        self.infobox = Infobox(self.screen, self.game_loop, self.fonts)

    def handle_event(self, events):
        for event in events:
            if event.type != pygame.KEYUP:
                continue

            if event.key == pygame.K_ESCAPE and self.game_loop.pause:
                self.game_loop.set_scene(EnumScenes.menu.value)
            if not self.game_loop.pause:
                for letter in self.game_loop.letters:
                    if chr(event.key) == letter.letter:
                        if self.game_loop.combo > 20:
                            self.game_loop.bullets.append(
                                Bullet3(self.screen, self.game_loop, letter.rect.x, self.sounds)
                            )
                        elif self.game_loop.combo > 10:
                            self.game_loop.bullets.append(
                                Bullet2(self.screen, self.game_loop, letter.rect.x, self.sounds)
                            )
                        else:
                            self.game_loop.bullets.append(
                                Bullet(self.screen, self.game_loop, letter.rect.x, self.sounds)
                            )
                        self.sounds[0].set_volume(random.uniform(0.2, 0.7))
                        pygame.mixer.Sound.play(self.sounds[0])
                        break

    def update(self):
        if self.game_loop.lifes <= 0:
            self.game_loop.set_scene(EnumScenes.game_over.value)

        if self.game_loop.points > 50 and self.game_loop.points%50 == 0:
            self.game_loop.level_up = 8
            self.game_loop.level = int(self.game_loop.points/50)

        match self.game_loop.level:
            case 2:
                self.game_loop.limit = 3
            case 3:
                self.game_loop.limit = 4
            case 4:
                self.game_loop.limit = 4
            case 5:
                self.game_loop.limit = 5
            case 6:
                self.game_loop.limit = 5
            case 7:
                self.game_loop.limit = 6
            case 8:
                self.game_loop.limit = 7
            case 9:
                self.game_loop.limit = 7
        
        if self.game_loop.level > 10:
            self.game_loop.limit = 8

        for index, bullet in enumerate(self.game_loop.bullets):
            if bullet.delete:
                self.game_loop.bullets.pop(index)
                continue
            bullet.update()

        if self.game_loop.errors >= 10:
            self.game_loop.errors = 0
            self.game_loop.screen_shake = 9
            self.game_loop.damage = 9
            self.life_bar.substract_lifes()

        for index, letter in enumerate(self.game_loop.letters):
            letter.update()
            if letter.rect.y > (HEIGHT-150):
                self.game_loop.explosions.append(
                    Explosion(self.screen, (letter.rect.x, letter.rect.y))
                )
                pygame.mixer.Sound.play(self.sounds[1], fade_ms=5)
                self.game_loop.letters.pop(index)
                self.game_loop.screen_shake = 9
                self.game_loop.damage = 9
                self.life_bar.substract_lifes()
                break

    def draw(self):
        self.screen.fill(C_BLACK)
        if len(self.game_loop.letters) < self.game_loop.limit:
            if random.randint(0,1):
                if self.game_loop.level < 4:
                    letter_val = get_valid_letter(self.game_loop, self.game_loop.level_1)
                elif self.game_loop.level < 7:
                    letter_val = get_valid_letter(self.game_loop, self.game_loop.level_2)
                else:
                    letter_val = get_valid_letter(self.game_loop, self.game_loop.level_3)

                self.game_loop.letters.append(
                    LetterBox(
                        self.screen, self.game_loop, self.fonts, letter_val
                    )
                )
        
        for letter in self.game_loop.letters:
            letter.draw()

        for explosion in self.game_loop.explosions:
            explosion.draw()

        for bullet in self.game_loop.bullets:
            bullet.draw()

        self.board.draw()

        if self.game_loop.screen_shake > 0:
            self.game_loop.screen_shake -= 1
            self.render_offset[0] = random.randint(0,9) -4
            self.render_offset[0] = random.randint(0,9) -4
        else:
            self.render_offset[0] = 0
            self.render_offset[0] = 0

        self.screen.blit(
            pygame.transform.scale(self.screen, (WIDTH, HEIGHT)), 
            self.render_offset
        )
        self.points.draw()
        
        if self.game_loop.level_up > 0:
            self.level.level_up()

        self.level.draw()
        self.life_bar.draw()
        self.infobox.draw()