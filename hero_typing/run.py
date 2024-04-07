import pygame
from settings import HEIGHT, WIDTH
from game_loop import GameLoop
from src.objects.fonts import load_fonts
from src.scenes.enum_scene import EnumScenes
from src.scenes.menu import Menu
from src.scenes.game_over import GameOver
from src.scenes.main import MainGame
from src.scenes.placar import Placar
from src.scenes.credits import Credits

pygame.init()
pygame.display.set_caption('Hero Typing')
pygame.display.set_mode((WIDTH, HEIGHT))
pygame.key.set_repeat(200, 25)

screen = pygame.display.get_surface()
clock = pygame.time.Clock()
fonts = load_fonts()
game_loop = GameLoop()

game_menu = Menu(screen, game_loop, fonts)
game_over = GameOver(screen, game_loop, fonts)
main_game = MainGame(screen, game_loop, fonts)
placar = Placar(screen, game_loop, fonts)
credits = Credits(screen, game_loop, fonts)

pygame.display.toggle_fullscreen()
while game_loop.in_game:
    clock.tick(45)
    events = pygame.event.get()
    game_loop.handle_event(events)

    match game_loop.scene:
        case EnumScenes.menu.value:
            game_menu.handle_event(events)
            game_menu.draw()
        case EnumScenes.game_over.value:
            game_over.handle_event(events)
            game_over.draw()
        case EnumScenes.main.value:
            main_game.handle_event(events)
            if not game_loop.pause:
                main_game.update()
            main_game.draw()
        case EnumScenes.placar.value:
            placar.handle_event(events)
            placar.draw()
        case EnumScenes.credits.value:
            credits.handle_event(events)
            credits.update()
            credits.draw()
    
    pygame.display.update()
