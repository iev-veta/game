import pygame as pg
import sys



class GameWin:
    def __init__(self):
        pg.init()
        self.WIDTH = 1200
        self.HEIGHT = 700
        self.screen = pg.display.set_mode((self.WIDTH, self.HEIGHT))
        pg.display.set_caption('Breakout')

        self.image = pg.transform.scale(pg.image.load('bg.jpg').convert(),
                                        (self.WIDTH, self.HEIGHT))

        self.button_font = pg.font.Font(None, 36)

        self.start_button = self.button_font.render("УРА СТИПЕНДИЯ!", True, (255, 255, 255))
        self.start_button_rect = self.start_button.get_rect(center=(self.WIDTH // 2, 300))

    def update(self):
        pg.display.flip()


    def draw(self):
        self.screen.blit(self.image, (0, 0))
        self.screen.blit(self.start_button, self.start_button_rect)


    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
        return True

    def run(self):
        while self.check_events():

            self.update()
            self.draw()

