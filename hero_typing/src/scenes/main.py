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

class MainGame():

    render_offset = [0,0]
    screen_shake = 0

    def __init__(self, screen, game_loop, fonts) -> None:
        self.screen = screen
        self.game_loop = game_loop
        self.fonts = fonts
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
                errou = False
                for index, letter in enumerate(self.game_loop.letters):
                    if event.key == letter.letter:
                        self.game_loop.combo += 1
                        letter.life_count -= 1
                        self.screen_shake = 9
                        if letter.life_count <= 0:
                            self.game_loop.explosions.append(
                                Explosion(self.screen, (letter.rect.x, letter.rect.y))
                            )
                            self.game_loop.letters.pop(index)
                            self.game_loop.points += self.game_loop.letter_value
                        break
                    elif event.key >=97 and event.key <=122:
                        errou = True
                if errou: 
                    if self.game_loop.combo < 1:
                        self.game_loop.ammo_error += 1
                    self.game_loop.combo = 0
                    if self.game_loop.ammo_error > 10:
                        self.game_loop.ammo_error = 0
                        self.life_bar.substract_lifes()

    def update(self):
        if self.game_loop.lifes <= 0:
            self.game_loop.set_scene(EnumScenes.game_over.value)

        if self.game_loop.points > 10 and self.game_loop.points%10 == 0 and self.game_loop.points < 100:
            self.game_loop.limit = self.game_loop.points/10

        if self.game_loop.points > 50 and self.game_loop.points%50 == 0:
            self.game_loop.level_up = 10
            self.game_loop.level = int(self.game_loop.points/50)

        match self.game_loop.level:
            case 2:
                self.game_loop.limit = 4
                self.game_loop.velocity = 2
            case 3:
                self.game_loop.limit = 6
                self.game_loop.velocity = 2
            case 4:
                self.game_loop.limit = 8
                self.game_loop.velocity = 2
            case 5:
                self.game_loop.limit = 10
                self.game_loop.velocity = 2
            case 6:
                self.game_loop.limit = 4
                self.game_loop.velocity = 3
            case 7:
                self.game_loop.limit = 6
                self.game_loop.velocity = 3
            case 8:
                self.game_loop.limit = 8
                self.game_loop.velocity = 3
            case 9:
                self.game_loop.limit = 10
                self.game_loop.velocity = 3
        
        if self.game_loop.level > 10:
            self.game_loop.limit = 12
            self.game_loop.velocity = 4

        for index, letter in enumerate(self.game_loop.letters):
            letter.update()
            if letter.rect.y > (HEIGHT-250):
                self.game_loop.explosions.append(
                    Explosion(self.screen, (letter.rect.x, letter.rect.y))
                )
                self.game_loop.letters.pop(index)
                self.game_loop.points += self.game_loop.letter_value
                self.screen_shake = 9
                self.game_loop.damage = 9
                self.life_bar.substract_lifes()
                break

    def draw(self):
        self.screen.fill(C_BLACK)
        print(self.game_loop.letters)
        if len(self.game_loop.letters) < self.game_loop.limit:
            if random.randbytes(1):
                self.game_loop.letters.append(
                    LetterBox(
                        self.screen, self.game_loop, self.fonts, random.randint(97,122)
                    )
                )
        
        for letter in self.game_loop.letters:
            letter.draw()

        for explosion in self.game_loop.explosions:
            explosion.draw()

        self.board.draw()

        if self.screen_shake > 0:
            self.screen_shake -= 1
            self.render_offset[0] = random.randint(0,8) -4
            self.render_offset[0] = random.randint(0,8) -4
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