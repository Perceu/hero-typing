import pygame


class GameLoop():

    in_game = True
    scene = 'menu'

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