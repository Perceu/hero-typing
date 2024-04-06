import pygame
from settings import C_BLACK, C_WHITE, C_GREEN, WIDTH,HEIGHT

def select_second_character(placar):
     return placar['placar']

class Placar(): 

    def __init__(self, screen, game_loop, fonts) -> None:
        self.screen = screen
        self.fonts = fonts
        self.game_loop = game_loop
    
    def load(self):
        with open("placar.txt", 'r') as file:
            placares = file.readlines()
        self.placares = []
        for placar in placares:
            nome, valor = placar.split(';')
            if int(valor) > 0:
                self.placares.append({
                    'nome': nome.strip().upper(),
                    'placar': int(valor.strip())
                })
        self.placares = reversed(sorted(self.placares, key=select_second_character))

    def handle_event(self, events):
        for event in events:
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    self.game_loop.set_scene('menu')

    def update(self):
        pass

    def draw(self):
        self.load()
        self.screen.fill(C_BLACK)
        center_width = WIDTH/2
        center_height = HEIGHT/2
        
        img = self.fonts['font_size_2'].render("Score  Player", True, C_GREEN)       
        self.screen.blit(img, (center_width-(img.get_width()/2), 10))


        for idx, placar in enumerate(self.placares):
            img_white = self.fonts["font_size_2"].render(f"{str(placar['placar']).zfill(4)}   {placar['nome']}", True, C_WHITE)
            self.screen.blit(img_white, (center_width-(img.get_width()/2), (35+((idx+1)*40))))