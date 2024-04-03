from time import sleep

import pygame as pg
import sys


restart = True

class GameOver:
    def __init__(self):
        pg.init()
        self.WIDTH = 1200
        self.HEIGHT = 700
        self.screen = pg.display.set_mode((self.WIDTH, self.HEIGHT))
        pg.display.set_caption('Breakout')

        self.image = pg.transform.scale(pg.image.load('bg.jpg').convert(),
                                        (self.WIDTH, self.HEIGHT))

        self.button_font = pg.font.Font(None, 36)

        self.start_button = self.button_font.render("Вы проиграли!", True, (255, 255, 255))
        self.start_button_rect = self.start_button.get_rect(center=(self.WIDTH // 2, 300))

        self.restart_button = self.button_font.render("Начать заново", True, (255, 255, 255))
        self.restart_button_rect = self.restart_button.get_rect(center=(self.WIDTH // 2, 400))

    def update(self):
        pg.display.flip()


    def draw(self):
        self.screen.blit(self.image, (0, 0))
        self.screen.blit(self.start_button, self.start_button_rect)
        # self.screen.blit(self.restart_button, self.restart_button_rect)

    def attention(self):
        self.screen.fill(pg.Color('black'))  # Красим фон в чёрный
        start_button = self.button_font.render("Приготовьтесь!", True, (255, 255, 255))
        start_button_rect = start_button.get_rect(center=(self.WIDTH // 2, 300))
        self.screen.blit(start_button, start_button_rect)
        pg.display.flip()

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            # if event.type == pg.MOUSEBUTTONDOWN:
            #     if self.restart_button_rect.collidepoint(event.pos):
            #
            #         self.attention()
            #
            #         sleep(1)  # ждём 3 секунды
            #         Restart().run()
            #         return False

        return True

    def run(self):
        while self.check_events():

            self.update()
            self.draw()

