import pygame
import random
from settings import C_GREEN, C_BLACK, C_WHITE, C_YELLOW, C_RED, HEIGHT, WIDTH,  C_BLUE
from scenes.menu import Menu
from game_loop import GameLoop
from elements.explosion import Explosion
from elements.letter import LetterBox
from elements.lifes import Lifes
from scenes.game_over import GameOver
from scenes.placar import Placar

pygame.init()
pygame.display.set_caption('Hero Typing')
pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.toggle_fullscreen()
pygame.key.set_repeat(200, 25)

screen = pygame.display.get_surface()
clock = pygame.time.Clock()

points = 0
damage = 0
screen_shake = 0
limit = 5
level = 1
combo = 0
letters = []
explosions = []
render_offset = [0,0]

fonts = {
    'font_size_4': pygame.font.SysFont('./assets/font/retro_gaming.ttf', 64),
    'font_size_3': pygame.font.SysFont('./assets/font/retro_gaming.ttf', 48),
    'font_size_2': pygame.font.SysFont('./assets/font/retro_gaming.ttf', 32),
    'font_size_1': pygame.font.SysFont('./assets/font/retro_gaming.ttf', 16),
}

game_loop = GameLoop()

game_over = GameOver(screen, fonts['font_size_3'])

placar = Placar(screen, fonts['font_size_2'], game_loop)

game_menu = Menu(fonts, game_loop)

life_bar = Lifes(screen, 1)

bonus = 1
pause = False

while game_loop.in_game:
    clock.tick(45)
    events = pygame.event.get()

    if game_loop.scene == 'game_over':
        game_over.handle_event(events)

    for event in events:
        game_loop.handle_event(event)
        game_menu.handle_event(event)

        if game_loop.scene == 'game_over' and not game_over.show_input:
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_r:
                    points = 0
                    damage = 0
                    screen_shake = 0
                    limit = 3
                    level = 1
                    letters.clear()
                    life_bar = Lifes(screen, 1)
                    game_loop.set_scene('main')
                elif event.key == pygame.K_s:
                    game_loop.set_scene('menu')
        
        elif game_loop.scene == 'main': 
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    pause = not pause
                new_point = False
                if not pause:
                    for index, letter in enumerate(letters):
                        if event.key == letter.letter:
                            explosions.append(Explosion(screen, (letter.x, letter.y)))
                            combo += 1
                            new_point = True
                            screen_shake = 9
                            letters.pop(index)
                            bonus = 1 if combo < 25 else int(combo/25)
                            if bonus > 10:
                                bonus = 10
                            points += bonus
                            break
                    if not new_point:
                        combo = 0
                else:
                    for index, letter in enumerate(letters):
                        if event.key == pygame.K_ESCAPE:
                            game_loop.set_scene('menu')
                            break
                    if not new_point:
                        combo = 0
                    
        
    if game_loop.scene == 'menu':
        game_menu.draw(screen)
    elif game_loop.scene == 'placar':
        placar.update(events)
        placar.draw()
    elif game_loop.scene == 'main':
        screen.fill(C_BLACK)
        cenario = pygame.Rect(200, 0, WIDTH-400, HEIGHT)
        life_bar.draw()
        points_img = fonts['font_size_3'].render(str(points).zfill(4), True, C_GREEN)
        screen.blit(points_img, (10, 10))
        img = fonts['font_size_1'].render(f"Level: {str(level).zfill(3)}", True, C_YELLOW)
        screen.blit(img, (10, 45))
        
        img_combo = fonts['font_size_1'].render("sequencia", True, C_WHITE)
        screen.blit(img_combo, (WIDTH-90, 10))
        img_combo = fonts['font_size_2'].render(f"{str(combo).zfill(3)}", True, C_BLUE)
        screen.blit(img_combo, (WIDTH-90, 20))
        img_combo = fonts['font_size_1'].render("Pontos p/ Acerto", True, C_WHITE)
        screen.blit(img_combo, (WIDTH-90, 45))
        img_combo = fonts['font_size_2'].render(f"{str(bonus).zfill(3)}", True, C_YELLOW)
        screen.blit(img_combo, (WIDTH-90, 55))

        img_combo = fonts['font_size_1'].render(f"{pause}", True, C_WHITE)
        screen.blit(img_combo, (WIDTH-90, 80))

        if life_bar.lifes <= 0 and damage <= 0 and screen_shake <= 0:
            game_loop.set_scene('game_over')
            continue
        
        if len(letters) < limit:
            if random.choice([0,1,0,1,0,1]):
                letters.append(LetterBox(screen,random.randint(97,122), fonts['font_size_2']))

        for index, letter in enumerate(letters):
            if letter.y >= HEIGHT:
                letters.pop(index)
                life_bar.substract_lifes()
                damage = 7
                screen_shake = 7
            if not pause:
                letter.update()
            letter.draw()

        if damage > 0:
            damage -= 1
            pygame.draw.rect(screen, C_RED, cenario,  2)
        else:
            pygame.draw.rect(screen, C_WHITE, cenario,  2)
        
        if screen_shake > 0:
            screen_shake -= 1
            render_offset[0] = random.randint(0,8) -4
            render_offset[0] = random.randint(0,8) -4
        else:
            render_offset[0] = 0
            render_offset[0] = 0

        if not points%10 and points > 20:
            limit = int((points+10)/10)
            level = int((points+10)/10)
        
        if not points%50 and points > 50:
            velocity = int((points+100)/100)

        for explosion in explosions:
            if explosion.running:
                explosion.draw()

        screen.blit(pygame.transform.scale(screen, (WIDTH, HEIGHT)), render_offset)
    elif game_loop.scene == 'game_over':
        game_over.draw(points)

    pygame.display.update()
