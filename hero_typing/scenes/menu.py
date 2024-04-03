import pygame
from pygame.font import SysFont
from settings import C_BLACK, C_WHITE, WIDTH, HEIGHT, C_GREEN


class Menu:
    fonts = dict[str, SysFont]
    menu_itens = [
        {'text': 'Iniciar', 'active': True, 'scene': 'main'},
        {'text': 'Placar', 'active': False, 'scene': 'placar'},
        {'text': 'Creditos', 'active': False, 'scene': 'game_over'},
        {'text': 'Sair', 'active': False, 'scene': 'quit'},
    ]

    def __init__(self, fonts, game_loop) -> None:
        self.fonts = fonts
        self.game_loop = game_loop

    def handle_event(self, event):
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RETURN:
                for idx, menu in enumerate(self.menu_itens):
                    if menu['active']:
                        if menu['scene'] == 'quit':
                            self.game_loop.quit()
                            break
                        else:
                            self.game_loop.set_scene(menu['scene'])
                            break

            if event.key == pygame.K_UP:
                for idx, menu in enumerate(self.menu_itens):
                    if menu['active']:
                       self.menu_itens[idx]['active'] = False
                       self.menu_itens[idx-1]['active'] = True
                       break
            
            elif event.key == pygame.K_DOWN:
                for idx, menu in enumerate(self.menu_itens):
                    if menu['active']:
                       self.menu_itens[idx]['active'] = False
                       self.menu_itens[(idx+1)%4]['active'] = True
                       break

    def draw(self, screen):
        screen.fill(C_BLACK)
        title = self.fonts["font_size_60"].render("Hero Typing", True, C_WHITE)
        width_title = (WIDTH / 2) - (title.get_width() / 2)
        height_title = (HEIGHT / 2) - title.get_height() - 100
        screen.blit(title, (width_title, height_title))


        for index, menu_item in enumerate(self.menu_itens):
            if menu_item["active"]:
                color = C_GREEN
            else:
                color = C_WHITE

            item = self.fonts["font_size_30"].render(menu_item["text"], True, color)
            width_item = (WIDTH / 2) - (item.get_width() / 2)
            height_item = (HEIGHT / 2) - item.get_height()
            screen.blit(item, (width_item, height_item + (index * 45)))
