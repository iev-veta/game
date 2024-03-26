import pygame as pg


class Paddle:
    def __init__(self, root):
        self.game = root
        self.paddle_w = 250
        self.paddle_h = 30
        self.paddle_speed = 7
        self.rect = pg.Rect(root.WIDTH // 2 - self.paddle_w // 2,
                            root.HEIGHT - self.paddle_h - 10,
                            self.paddle_w, self.paddle_h)

        self.color = pg.Color(200, 130, 50)

    def draw(self):
        pg.draw.rect(self.game.screen, self.color, self.rect)

    def update(self):
        key = pg.key.get_pressed()
        if key[pg.K_LEFT] and self.rect.left > 0:
            self.rect.left -= self.paddle_speed

        elif key[pg.K_RIGHT] and self.rect.right < self.game.WIDTH:
            self.rect.right += self.paddle_speed
