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
    letters = []
    explosions = []
    bullets = []
    combo = 0
    damage = 0
    level_up = 0
    screen_shake = 0
    bonus = ['0','1','2','3','4','5','6','7','8','9']
    level_1 = ['a','s','d','f','g','h','j','k','l']
    level_2 = level_1+['q','w','e','r','t','y','u','i','o','p']
    level_3 = level_2+['z','x','c','v','b','n','m']

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
