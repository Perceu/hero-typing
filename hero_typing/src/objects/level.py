import pygame
from settings import WIDTH, C_BLACK, C_RED, HEIGHT


class Level(): 
    def __init__(self, screen, game_loop, fonts) -> None:
        self.screen = screen
        self.game_loop = game_loop
        self.fonts = fonts

    def draw(self):
        level = self.game_loop.level
        rect = pygame.Rect(0, HEIGHT-80, WIDTH, 100)
        img = self.fonts['font_size_2'].render(
            f"Level: {str(level).zfill(3)}", True, C_RED
        )
        final_w = (WIDTH/2) - (img.get_width()/2)
        pygame.draw.rect(self.screen, C_BLACK, rect)
        self.screen.blit(img, (final_w, HEIGHT-100))
    
    def level_up(self):
        level = self.game_loop.level
        img_temp = self.fonts['font_size_2'].render(
            f"Level: {str(level).zfill(3)}", True, C_RED
        )
        img = self.fonts['font_size_4'].render('Level Up', True, C_RED)

        altura_inicial = (HEIGHT/2)-img.get_height()/2
        largura_inicial = (WIDTH/2)-img.get_width()/2

        altura_final = HEIGHT-100
        largura_final = (WIDTH/2) + img_temp.get_width()


        distance_l = largura_final - largura_inicial
        distance_a = altura_final - altura_inicial

        move_l = int((distance_l/9)*(9-self.game_loop.level_up))
        move_a = int((distance_a/9)*(9-self.game_loop.level_up))
        
        self.screen.blit(img, ((largura_inicial+move_l), (altura_inicial+move_a)))

        self.game_loop.level_up -= 1
