import pygame as pg
import sys
from random import randrange

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
   def __init__(self, root: Game):
      self.game = root  # поле игры
      self.paddle_w = 250  # ширина
      self.paddle_h = 30  # высота
      self.paddle_speed = 15  # скорость движения
      self.rect = pg.Rect(root.WIDTH // 2 - self.paddle_w // 2,
         root.HEIGHT - self.paddle_h - 10,
         self.paddle_w, self.paddle_h)  # рисуем в центре экрана снизу
      self.color = pg.Color(200, 130, 50)  # цвет прямоугольника

   def draw(self):
      pg.draw.rect(self.game.screen, self.color, self.rect)
      
   def update(self):
      key = pg.key.get_pressed()  # проверяем нажатые кнопки
      # если стрелка влево нажата и блок не ушёл за границу левую:
      if key[pg.K_LEFT] and self.rect.left > 0:
         self.rect.left -= self.paddle_speed
         # иначе если стрелка вправо нажата и блок не ушёл за границу правую:
      elif key[pg.K_RIGHT] and self.rect.right < self.game.WIDTH:
         self.rect.right += self.paddle_speed

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
