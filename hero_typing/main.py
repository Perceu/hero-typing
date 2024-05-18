import asyncio
import pygame
from pathlib import Path
from settings import HEIGHT, WIDTH
from game_loop import GameLoop
from src.objects.fonts import load_fonts
from src.scenes.enum_scene import EnumScenes
from src.scenes.menu import Menu
from src.scenes.game_over import GameOver
from src.scenes.main import MainGame
from src.scenes.placar import Placar
from src.scenes.credits import Credits
from src.scenes.options import Options


async def main():
    pygame.init()
    pygame.display.set_caption('Hero Typing')
    pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.key.set_repeat(200, 25)

    screen = pygame.display.get_surface()
    clock = pygame.time.Clock()
    fonts = load_fonts()
    game_loop = GameLoop()

    shot = pygame.mixer.Sound(Path.cwd().joinpath('hero_typing/media/shot.mp3'))
    explosion = pygame.mixer.Sound(Path.cwd().joinpath('hero_typing/media/explosion.mp3'))

    game_menu = Menu(screen, game_loop, fonts)
    game_over = GameOver(screen, game_loop, fonts)
    main_game = MainGame(screen, game_loop, fonts, (shot, explosion))
    placar = Placar(screen, game_loop, fonts)
    credits = Credits(screen, game_loop, fonts)
    options = Options(screen, game_loop, fonts)

    pygame.mixer.music.load(Path.cwd().joinpath('hero_typing/media/background.mp3'))
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play(-1)
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
            case EnumScenes.options.value:
                options.handle_event(events)
                options.update()
                options.draw()
        
        await asyncio.sleep(0)  # This line is critical; ensure you keep the sleep time at 0
        pygame.display.update()

asyncio.run(main())