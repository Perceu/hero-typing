from settings import WIDTH, HEIGHT, C_BLACK, C_GREEN, C_WHITE, C_RED


class GameOver(): 

    def __init__(self, screen, font) -> None:
        self.screen = screen
        self.font = font


    def draw(self, points):
        self.screen.fill(C_BLACK)

        img_white = self.font.render("Sua Pontuação:", True, C_WHITE)
        self.screen.blit(img_white, ((WIDTH/2)-(img_white.get_width()/2), HEIGHT-660))
        
        img_points = self.font.render(str(points).zfill(4), True, C_GREEN)
        self.screen.blit(img_points, ((WIDTH/2)-(img_points.get_width()/2), HEIGHT-600))
        
        img = self.font.render("GAME OVER", True, C_RED)
        self.screen.blit(img, ((WIDTH/2)-(img.get_width()/2), (HEIGHT/2)-img.get_height()))
        
        img_white_2 = self.font.render("[R]einiciar ou [S]air", True, C_WHITE)
        self.screen.blit(img_white_2, ((WIDTH/2)-(img_white_2.get_width()/2), HEIGHT-300))