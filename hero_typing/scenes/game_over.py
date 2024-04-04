import pygame
from pygame_textinput import TextInputVisualizer
from settings import WIDTH, HEIGHT, C_BLACK, C_GREEN, C_WHITE, C_RED
from faker import Faker

class GameOver(): 

    def __init__(self, screen, font) -> None:
        fake = Faker()
        self.points = 0
        self.screen = screen
        self.font = font
        self.show_input = True
        self.textinput = TextInputVisualizer()
        self.textinput.value = fake.name()
        self.textinput.font_color = [255,255,255]

    def handle_event(self, events):
        self.textinput.update(events)
        for event in events:
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RETURN:
                    self.show_input = False
                    with open("placar.txt", 'a') as file:
                        file.write(f"{self.textinput.value};{self.points}\n")

    def draw(self, points):
        self.points = points
        self.screen.fill(C_BLACK)
        center_width = int(WIDTH/2)
        center_height = int(HEIGHT/2)
        
        img = self.font.render("GAME OVER", True, C_RED)
        self.screen.blit(img, (center_width-(img.get_width()/2), center_height-img.get_height()))
        
        img = self.font.render("Pontuação", True, C_WHITE)
        self.screen.blit(img, (center_width-(img.get_width()/2), center_height-img.get_height()-150))
        
        img = self.font.render(str(points).zfill(4), True, C_GREEN)
        self.screen.blit(img, (center_width-(img.get_width()/2), center_height-img.get_height()-100))

        if self.show_input:
            img = self.font.render("Digite seu nick:", True, C_WHITE)
            self.screen.blit(img, (center_width-(img.get_width()/2), center_height-img.get_height()+100))
            self.textinput.surface.get_width()
            self.screen.blit(self.textinput.surface, (center_width-(self.textinput.surface.get_width()/2), center_height-self.textinput.surface.get_height()+200))
        else:
            img = self.font.render("[R]einiciar ou [S]air", True, C_WHITE)
            self.screen.blit(img, (center_width-(img.get_width()/2), center_height-img.get_height()+100))