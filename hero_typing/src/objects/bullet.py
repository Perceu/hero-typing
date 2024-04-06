from settings import HEIGHT

class Bullet():

    y = HEIGHT+2

    def __init__(self, explosion, x, y) -> None:
        self.dest_x = x
        self.dest_y = y
        self.explosion = explosion

    def update(self):
        if self.y > self.dest_y:
            self.y -= 1
        else
            self.explosion
    
    def draw(self):
        pass