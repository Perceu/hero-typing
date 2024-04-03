import pygame
from settings import C_BLACK, C_WHITE


class Placar(): 

    def __init__(self, screen, font) -> None:
        self.screen = screen
        self.font = font
    
    def load(self):
        with open("placar.txt", 'r') as file:
            placares = file.readlines()

        self.placares = []
        for placar in placares:
            nome, valor, _ = placar.split(';')
            self.placares.append({
                'nome': nome,
                'placar': valor
            })

    def draw(self):
        self.load()
        self.screen.fill(C_BLACK)
        for idx, placar in enumerate(self.placares):
            img_white = self.font.render(f"{idx+1} - {placar['nome']} -- {placar['placar']}", True, C_WHITE)
            self.screen.blit(img_white, (30, (30+(idx*20))))