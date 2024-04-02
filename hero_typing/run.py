import pygame
import random
from settings import C_GREEN, C_BLACK, C_WHITE, C_YELLOW, C_RED, HEIGHT, WIDTH, START_LIFES
from scenes.menu import Menu
from game_loop import GameLoop
from elements.explosion import Explosion
from elements.letter import LetterBox
from elements.lifes import Lifes
from scenes.game_over import GameOver

pygame.init()

screen = pygame.display.set_mode((HEIGHT, WIDTH))
clock = pygame.time.Clock()
points = 0
damage = 0
screen_shake = 0
limit = 3
level = 1
letters = []
explosions = []
render_offset = [0,0]

fonts = {
    'font_size_60': pygame.font.SysFont('./assets/font/retro_gaming.ttf', 60),
    'font_size_45': pygame.font.SysFont('./assets/font/retro_gaming.ttf', 45),
    'font_size_30': pygame.font.SysFont('./assets/font/retro_gaming.ttf', 30),
    'font_size_15': pygame.font.SysFont('./assets/font/retro_gaming.ttf', 15),
}

game_loop = GameLoop()
game_over = GameOver(screen, fonts['font_size_45'])
game_menu = Menu(fonts, game_loop)
life_bar = Lifes(screen, START_LIFES)

while game_loop.in_game:
    clock.tick(45)
    for event in pygame.event.get():
        game_loop.handle_event(event)
        game_menu.handle_event(event)
        for index, letter in enumerate(letters):
            if event.type == pygame.KEYUP:
                if event.key == letter.letter:
                    explosions.append(Explosion(screen, (letter.x, letter.y)))
                    screen_shake = 9
                    letters.pop(index)
                    points += 1
                    break
       
    if game_loop.scene == 'menu':
        game_menu.draw(screen)
    elif game_loop.scene == 'main':
        screen.fill(C_BLACK)
        cenario = pygame.Rect(100, 0, WIDTH-200, HEIGHT)
        life_bar.draw()
        points_img = fonts['font_size_45'].render(str(points).zfill(4), True, C_GREEN)
        screen.blit(points_img, (10, 10))
        img = fonts['font_size_15'].render(f"Level: {str(level).zfill(3)}", True, C_YELLOW)
        screen.blit(img, (10, 45))
        if life_bar.lifes <= 0:
            game_loop.set_scene('game_over')
            continue
        
        if len(letters) < limit:
            if random.choice([0,1,0,1,0,1]):
                letters.append(LetterBox(screen,random.randint(97,122), fonts['font_size_30']))

        for index, letter in enumerate(letters):
            if letter.y >= HEIGHT:
                letters.pop(index)
                life_bar.substract_lifes()
                damage = 7
                screen_shake = 7

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

        screen.blit(pygame.transform.scale(screen, (HEIGHT, WIDTH)), render_offset)
    elif game_loop.scene == 'game_over':
        game_over.draw(points)

    pygame.display.update()

# 
# velocity = 3
# level = 1
# limit = 2
# screen_shake = 0
# damage = 0
# render_offset = [0,0]

# cenario = pygame.Rect(100, 0, WIDTH-200, HEIGHT)

# def change_game_dificult():
#     global limit, velocity, level, points
#     img = level_font.render(f"Level: {str(level).zfill(3)}", True, C_YELLOW)
#     screen.blit(img, (10, 45))
#     if not points%10 and points > 20:
#         limit = int((points+10)/10)
#         level = int((points+10)/10)
    
#     if not points%50 and points > 50:
#         velocity = int((points+100)/100)

# game_over = GameOver(screen, points_final_font)
# 

        
    # screen.fill(C_BLACK)
    # clock.tick(45)
    # pygame.draw.rect(screen, C_WHITE, cenario,  2)
    
    # if damage > 0:
    #     damage -= 1
    #     pygame.draw.rect(screen, C_RED, cenario,  2)

    # for event in pygame.event.get():
    #     if event.type == pygame.QUIT:
    #        ingame = False 
    #     if event.type == pygame.KEYUP:
    #         if life_bar.lifes <= 0:
    #             if event.key == pygame.K_r:
    #                 life_bar = Lifes(screen, START_LIFES)
    #                 limit = 2
    #                 level = 1
    #                 points = 0
    #                 damage = 0
    #                 screen_shake = 0
    #                 letters.clear()
    #             if event.key == pygame.K_s:
    #                 ingame = False
    #         else:

    # if life_bar.lifes <= 0:
    #     game_over.draw(points)
    #     pygame.display.update()
    #     continue

    # if len(letters) < limit:
    #     if random.choice([0,1,0,1,0,1]):
    #         letters.append(LetterBox(screen,random.randint(97,122), letter_font))

    # for index, letter in enumerate(letters):
    #     if letter.y >= HEIGHT:
    #         letters.pop(index)
    #         life_bar.substract_lifes()
    #         damage = 7
    #         screen_shake = 7

    #     letter.update()
    #     letter.draw()

    # for explosion in explosions:
    #     if explosion.running:
    #         explosion.draw()

    # if screen_shake > 0:
    #     screen_shake -= 1
    #     render_offset[0] = random.randint(0,8) -4
    #     render_offset[0] = random.randint(0,8) -4
    # else:
    #     render_offset[0] = 0
    #     render_offset[0] = 0

    # screen.blit(pygame.transform.scale(screen, windown_size), render_offset)
    # life_bar.draw()
    # change_game_dificult()

    # pygame.display.update()
    # for key, explosion in enumerate(explosions):
    #     if not explosion.running:
    #         del(explosions[key])

