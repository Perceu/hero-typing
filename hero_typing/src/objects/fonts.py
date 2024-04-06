import pygame
from pathlib import Path

def load_fonts():
    return {
        'font_size_4': pygame.font.Font(Path.cwd().joinpath('hero_typing/src/objects/assets/retro_gaming.ttf'), 256),
        'font_size_3': pygame.font.Font(Path.cwd().joinpath('hero_typing/src/objects/assets/retro_gaming.ttf'), 128),
        'font_size_2': pygame.font.Font(Path.cwd().joinpath('hero_typing/src/objects/assets/retro_gaming.ttf'), 64),
        'font_size_1': pygame.font.Font(Path.cwd().joinpath('hero_typing/src/objects/assets/retro_gaming.ttf'), 32),
    }