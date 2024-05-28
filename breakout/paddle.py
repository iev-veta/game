import pygame as pg


class Paddle(pg.sprite.Sprite):
    def __init__(self, root):
        pg.sprite.Sprite.__init__(self)
        self.game = root
        self.paddle_w = 250 # 1200
        self.paddle_h = 30
        self.paddle_speed = 7

        self.image = pg.transform.scale(pg.image.load("pi/paddle.jpg").convert(), (250, 30))
        self.rect = self.image.get_rect(center=(root.WIDTH // 2 - self.paddle_w // 2,
                            root.HEIGHT - self.paddle_h - 10))

        self.color = pg.Color(200, 130, 50)

    def draw(self):
        self.game.screen.blit(self.image, self.rect)

    def update(self):
        key = pg.key.get_pressed()
        if key[pg.K_LEFT] and self.rect.left > 0:
            self.rect.left -= self.paddle_speed

        elif key[pg.K_RIGHT] and self.rect.right < self.game.WIDTH:
            self.rect.right += self.paddle_speed
