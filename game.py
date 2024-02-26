import pygame as pg
import sys

class Game:
   def init(self):
       pg.init()  # инициализация pygame
       self.WIDTH = 1200  # ширина
       self.HEIGHT = 700  # высота
       self.screen = pg.display.set_mode((self.WIDTH, self.HEIGHT))  # поле окна
       pg.display.set_caption('Breakout')  # название окна
       self.paddle = Paddle(self)  # создание поля подушки
       self.ball = Ball(self)  # создание поля мячика

       self.FPS = 60  # FPS
       self.clock = pg.time.Clock()  # поле счётчика времени

   def update(self):
       self.paddle.update()
       self.ball.update()
       pg.display.flip()
       self.clock.tick(self.FPS)

   def draw(self):
       self.paddle.draw()
       self.ball.draw()

   @staticmethod
   def check_events():
       for event in pg.event.get():
           if event.type == pg.QUIT:
               pg.quit()
               sys.exit()

   def run(self):
       while True:
           self.check_events()
           self.update()
           self.draw()


class Paddle:
   def init(self, root: Game):
       pass

   def draw(self):
       pass

   def update(self):
       pass

class Ball:
   def init(self, root: Game):
       pass

   def draw(self):
       pass

   def update(self):
       pass

if name == 'main':
   game = Game()
   game.run()