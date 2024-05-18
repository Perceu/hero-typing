import pygame
from settings import WIDTH, HEIGHT, C_GREEN, C_RED, C_WHITE


class Infobox(): 
    def __init__(self, screen, game_loop, fonts) -> None:
        self.screen = screen
        self.game_loop = game_loop
        self.fonts = fonts

    def draw(self):
        img = self.fonts['font_size_2'].render("Combo:", True, C_GREEN)
        self.screen.blit(img, (WIDTH-280, 50))
        img = self.fonts['font_size_2'].render(str(self.game_loop.combo).zfill(4), True, C_WHITE)
        self.screen.blit(img, (WIDTH-280, 80))

        img = self.fonts['font_size_2'].render("Error:", True, C_RED)
        self.screen.blit(img, (WIDTH-280, 180))
        img = self.fonts['font_size_2'].render(str(self.game_loop.errors).zfill(4), True, C_WHITE)
        self.screen.blit(img, (WIDTH-280, 220))
        
        if self.game_loop.pause:
            surface = pygame.Surface((WIDTH,HEIGHT))
            surface.fill((255, 255, 255))
            surface.set_alpha(50)
            img = self.fonts['font_size_2'].render('PAUSED', True, C_RED)
            self.screen.blit(surface, (0,0))
            self.screen.blit(img, (((WIDTH/2)-img.get_width()/2), ((HEIGHT/2)-img.get_height()/2)))
    
    def level_up():
        pass