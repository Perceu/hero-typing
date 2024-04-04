import pygame
from settings import C_BLACK, C_WHITE, C_GREEN

def select_second_character(placar):
     return placar['placar']

class Placar(): 

    def __init__(self, screen, font, game_loop) -> None:
        self.screen = screen
        self.font = font
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

    def update(self, events):
        for event in events:
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    self.game_loop.set_scene('menu')

    def draw(self):
        self.load()
        self.screen.fill(C_BLACK)
        img_white = self.font.render("Score  Player", True, C_GREEN)
        self.screen.blit(img_white, (30, 30))

        for idx, placar in enumerate(self.placares):
            img_white = self.font.render(f"{str(placar['placar']).zfill(4)}   {placar['nome']}", True, C_WHITE)
            self.screen.blit(img_white, (30, (35+((idx+1)*25))))