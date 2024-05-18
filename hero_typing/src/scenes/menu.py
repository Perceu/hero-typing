import pygame
from pygame.font import SysFont
from settings import C_BLACK, C_WHITE, WIDTH, HEIGHT, C_GREEN


class Menu:
    fonts = dict[str, SysFont]
    active_menu = {'text': 'Iniciar', 'active': True, 'scene': 'main'}
    menu_itens = [
        {'text': 'Iniciar', 'active': True, 'scene': 'main'},
        {'text': 'Placar', 'active': False, 'scene': 'placar'},
        {'text': 'Creditos', 'active': False, 'scene': 'credits'},
        {'text': 'Options', 'active': False, 'scene': 'options'},
        {'text': 'Sair', 'active': False, 'scene': 'quit'},
    ]

    def __init__(self, screen, game_loop, fonts) -> None:
        self.screen = screen
        self.fonts = fonts
        self.game_loop = game_loop

    def handle_event(self, events):
        for event in events:
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RETURN:
                    if self.active_menu['scene'] == 'quit':
                        self.game_loop.quit()
                    else:
                        self.game_loop.set_scene(self.active_menu['scene'])

                if event.key == pygame.K_UP:
                    for idx, menu in enumerate(self.menu_itens):
                        if menu['active']:
                            self.menu_itens[idx]['active'] = False
                            self.menu_itens[idx-1]['active'] = True
                            self.active_menu = self.menu_itens[idx-1]
                            break
                
                elif event.key == pygame.K_DOWN:
                    for idx, menu in enumerate(self.menu_itens):
                        if menu['active']:
                            self.menu_itens[idx]['active'] = False
                            self.menu_itens[(idx+1)%len(self.menu_itens)]['active'] = True
                            self.active_menu = self.menu_itens[(idx+1)%len(self.menu_itens)]
                            break

    def draw(self):
        self.screen.fill(C_BLACK)
        title = self.fonts["font_size_4"].render("Hero Typing", True, C_WHITE)
        width_title = (WIDTH / 2) - (title.get_width() / 2)
        height_title = (HEIGHT / 2) - title.get_height() - 100
        self.screen.blit(title, (width_title, height_title))


        for index, menu_item in enumerate(self.menu_itens):
            if menu_item["active"]:
                color = C_GREEN
            else:
                color = C_WHITE

            item = self.fonts["font_size_2"].render(menu_item["text"], True, color)
            width_item = (WIDTH / 2) - (item.get_width() / 2)
            height_item = (HEIGHT / 2) - item.get_height()
            self.screen.blit(item, (width_item, height_item + (index * 45)))
