import pygame as pg
import sys
from random import randrange
from game_over import GameOver
from game_win import GameWin

from ball import Ball
from paddle import Paddle


class Game:
    def __init__(self):
        pg.init()
        self.WIDTH = 1200
        self.HEIGHT = 700
        self.screen = pg.display.set_mode((self.WIDTH, self.HEIGHT))
        pg.display.set_caption('Breakout')
        self.paddle = Paddle(self)
        self.ball = Ball(self)

        self.FPS = 60  # FPS
        self.clock = pg.time.Clock()

        self.image = pg.transform.scale(pg.image.load('bg.jpg').convert(),
                                        (self.WIDTH, self.HEIGHT))

        self.block_list = [pg.Rect(10 + 120 * i,
                                   10 + 70 * j,
                                   100,
                                   50) for i in range(10) for j in range(4)]

        self.color_list = [(randrange(30, 256),
                            randrange(30, 256),
                            randrange(30, 256)) for _ in range(10) for _ in range(4)]

    def update(self):
        self.paddle.update()
        self.ball.update()
        pg.display.flip()
        self.clock.tick(self.FPS)

    def draw(self):
        self.screen.blit(self.image, (0, 0))

        for color, block in enumerate(self.block_list):
            pg.draw.rect(self.screen, self.color_list[color], block)

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
