import pygame as pg
import sys
import random
from game_over import GameOver
from game_win import GameWin

from ball import Ball
from paddle import Paddle


class Pic(pg.sprite.Sprite):
    def __init__(self,game, pic, x, y):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.transform.scale(pg.image.load(pic).convert(), (100, 50))
        self.rect = self.image.get_rect(center=(x, y))
        self.game = game

    def draw(self):
        self.game.screen.blit(self.image, self.rect)







class Game:
    def __init__(self):
        pg.init()
        self.WIDTH = 1200
        self.HEIGHT = 700
        self.screen = pg.display.set_mode((self.WIDTH, self.HEIGHT))
        pg.display.set_caption('ГОЛОДНЫЕ ИГРЫ СТУДЕНТОВ МИРЭА')
        self.paddle = Paddle(self)
        self.ball = Ball(self)

        self.FPS = 60  # FPS
        self.clock = pg.time.Clock()

        self.image = pg.transform.scale(pg.image.load('bg.jpg').convert(),
                                        (self.WIDTH, self.HEIGHT))

        self.bloks = pg.sprite.Group()
        for i in range(10):
            for j in range(3):
                self.bloks.add()

        self.block_list = [Pic(self,f'pi/{random.randint(1,30)}.jpg', 60 + 120 * i,
                               10 + 70 * j) for i in range(10) for j in range(3)]

    def update(self):
        self.paddle.update()
        self.ball.update()
        pg.display.flip()
        self.clock.tick(self.FPS)

    def draw(self):
        self.screen.blit(self.image, (0, 0))

        for block in self.block_list:
            block.draw()

        self.paddle.draw()
        self.ball.draw()

    def check_game_over(self):
        if self.ball.ball.bottom > self.HEIGHT:
            GameOver().run()
        elif not len(self.block_list):
            GameWin().run()

    @staticmethod
    def check_events():
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

    def run(self):
        while True:
            self.check_game_over()
            self.check_events()
            self.update()
            self.draw()
