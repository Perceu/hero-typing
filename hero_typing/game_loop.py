import pygame


class GameLoop():
    in_game = True
    pause = False
    
    player = None
    
    scene = 'menu'
    
    points = 0
    errors = 0

    level = 1
    limit = 2
    velocity = 1
    lifes = 6

    letter_value = 1
    
    letters = []
    explosions = []
    bullets = []

    combo = 0
    ammo_error = 0

    damage = 0
    level_up = 0
    screen_shake = 0

    def handle_event(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                self.quit()
            
            if event.type != pygame.KEYUP:
                continue

            if event.key == pygame.K_SPACE:
                self.pause = not self.pause

    def quit(self):
        self.in_game = False

    def set_scene(self, scene):
        self.scene = scene

    def restart_game(self):
        self.in_game = True
        self.player = None
        self.scene = 'menu'
        self.lifes = 6
        self.limit = 2
        self.level = 1
        self.points = 0
        self.combo = 0
        self.damage = 0
        self.screen_shake = 0
        self.level_up = 0
        self.letters = []
        self.explosions = []
        self.bullets = []
