from enum import Enum
import pygame


class EnumScenes(Enum):
    main = 'main'
    game_over = 'game_over'
    menu = 'menu'
    placar = 'placar'


class GameLoop():

    in_game = True
    scene = EnumScenes.menu.value

    def handle_event(self, event):
        if event.type == pygame.QUIT:
           self.in_game = False
        return True
    
    def quit(self):
        self.in_game = False
        return True
    
    def set_scene(self, scene):
        self.scene = scene
        return True