import random
import pygame
import math


class Explosion():

    def __init__(self, screen, position):
        self.screen = screen
        self.position_initial = position
        self.frame = 1
        self.running = True
        self.color = []
        self.color.append((255,255,255))

    def increment_postion(self, increment_position):
        return tuple(y+x for y, x in zip(self.position_initial, increment_position))

    def draw_circle(self, position, size):
        pygame.draw.circle(self.screen, self.color[0], position, size)

    def defrag_circle(self, num_circles, position_distance, size):
        for i in range(1, num_circles):
            distance = random.randint(position_distance[0],position_distance[1])
            angle = (360/num_circles)*i
            position = (int(math.cos(angle)*distance), int(math.sin(angle)*distance))
            self.draw_circle(self.increment_postion(position), size)
       

    def draw(self):
        
        if self.frame == 1:
            self.defrag_circle(num_circles = 1, position_distance = (0,2), size = 2)
            self.frame += 1
        elif self.frame == 2:
            self.defrag_circle(num_circles = 2, position_distance = (0,2), size = 5)
            self.frame += 1
        elif self.frame == 3:
            self.defrag_circle(num_circles = 3, position_distance = (2,8), size = 10)
            self.frame += 1   
        elif self.frame == 4:
            self.defrag_circle(num_circles = 4, position_distance = (5,18), size = 15)
            self.frame += 1   
        elif self.frame == 5:
            self.defrag_circle(num_circles = 5, position_distance = (12,27), size = 20)
            self.frame += 1   
        elif self.frame == 6:
            self.defrag_circle(num_circles = 6, position_distance = (25,36), size = 15)
            self.frame += 1    
        elif self.frame == 7:
            self.defrag_circle(num_circles = 7, position_distance = (35,40), size = 10)
            self.frame += 1   
        elif self.frame == 8:
            self.defrag_circle(num_circles = 8, position_distance = (42,53), size = 5)
            self.frame += 1   
        elif self.frame == 9:
            self.defrag_circle(num_circles = 9, position_distance = (52,70), size = 2)
            self.frame += 1   
        else:
            if self.frame > 9:
                self.running = False