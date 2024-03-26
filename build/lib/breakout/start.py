from time import sleep

import pygame as pg
import sys



class Start:
    def __init__(self):
        pg.init()
        self.WIDTH = 1200
        self.HEIGHT = 700
        self.screen = pg.display.set_mode((self.WIDTH, self.HEIGHT))
        pg.display.set_caption('Breakout')

        self.image = pg.transform.scale(pg.image.load('bg.jpg').convert(),
                                        (self.WIDTH, self.HEIGHT))

        self.button_font = pg.font.Font(None, 36)

        self.start_button = self.button_font.render("Старт игры", True, (255, 255, 255))
        self.start_button_rect = self.start_button.get_rect(center=(self.WIDTH // 2, 300))

        self.exit_button = self.button_font.render("Выйти", True, (255, 255, 255))
        self.exit_button_rect = self.exit_button.get_rect(center=(self.WIDTH // 2, 400))

    def update(self):
        pg.display.flip()


    def draw(self):
        self.screen.blit(self.image, (0, 0))
        self.screen.blit(self.start_button, self.start_button_rect)
        self.screen.blit(self.exit_button, self.exit_button_rect)

    def attention(self):
        self.screen.fill(pg.Color('black'))  # Красим фон в чёрный
        start_button = self.button_font.render("Приготовьтесь!", True, (255, 255, 255))
        start_button_rect = start_button.get_rect(center=(self.WIDTH // 2, 300))
        self.screen.blit(start_button, start_button_rect)
        pg.display.flip()  # обновляем экран

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if self.start_button_rect.collidepoint(event.pos):

                    self.screen.fill(pg.Color('black'))  # Красим фон в чёрный
                    self.attention()


                    sleep(5)  # ждём 3 секунды
                    return False
                if self.exit_button_rect.collidepoint(event.pos):
                    pg.quit()
                    sys.exit()

        return True

    def run(self):
        while self.check_events():

            self.update()
            self.draw()
