import pygame
from pygame_textinput import TextInputVisualizer
from settings import WIDTH, HEIGHT, C_BLACK, C_GREEN, C_WHITE, C_RED
from faker import Faker


class GameOver(): 

    def __init__(self, screen, game_loop, fonts) -> None:
        fake = Faker()
        self.screen = screen
        self.fonts = fonts
        self.game_loop = game_loop
        self.show_input = True
        self.textinput = TextInputVisualizer()
        self.textinput.value = fake.name()
        self.textinput.font_color = [255,255,255]

    def handle_event(self, events):
        self.textinput.update(events)
        if self.game_loop.player:
            self.show_input = False
            self.textinput.value = self.game_loop.player
        else:
            self.show_input = True

        for event in events:
            if event.type != pygame.KEYUP:
                continue
            
            if event.key == pygame.K_RETURN:
                self.show_input = False
                self.game_loop.player = self.textinput.value
                if self.points <= 0:
                    continue
                with open("placar.txt", 'a') as file:
                    file.write(f"{self.textinput.value};{self.points}\n")
            elif event.key == pygame.K_s and not self.show_input:
                self.game_loop.quit()
            elif event.key == pygame.K_m and not self.show_input:
                self.game_loop.restart_game()

    def draw(self):
        self.points = self.game_loop.points
        self.screen.fill(C_BLACK)
        center_width = int(WIDTH/2)
        center_height = int(HEIGHT/2)
        
        img = self.fonts['font_size_2'].render("GAME OVER", True, C_RED)
        self.screen.blit(img, (center_width-(img.get_width()/2), center_height-img.get_height()))
        
        img = self.fonts['font_size_2'].render("Score", True, C_WHITE)
        self.screen.blit(img, (center_width-(img.get_width()/2), center_height-img.get_height()-150))
        
        img = self.fonts['font_size_2'].render(str(self.points).zfill(4), True, C_GREEN)
        self.screen.blit(img, (center_width-(img.get_width()/2), center_height-img.get_height()-100))

        if self.show_input:
            img = self.fonts['font_size_2'].render("Player name:", True, C_WHITE)
            self.screen.blit(img, (center_width-(img.get_width()/2), center_height-img.get_height()+100))
            self.textinput.surface.get_width()
            self.screen.blit(self.textinput.surface, (center_width-(self.textinput.surface.get_width()/2), center_height-self.textinput.surface.get_height()+200))
        else:
            img = self.fonts['font_size_2'].render("[M]enu [S]air", True, C_WHITE)
            self.screen.blit(img, (center_width-(img.get_width()/2), center_height-img.get_height()+100))