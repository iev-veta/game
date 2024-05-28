from random import randrange

import pygame as pg


class Ball(pg.sprite.Sprite):
    def __init__(self, root):
        pg.sprite.Sprite.__init__(self)
        self.game = root
        self.radius = 10
        self.speed = 5

        self.rect = int(self.radius * 2 ** 0.5)

        self.image = pg.transform.scale(pg.image.load("pi/ball.png"), (20, 20))
        self.ball = self.image.get_rect(center=(randrange(self.rect, self.game.WIDTH - self.rect),
                            self.game.HEIGHT // 2))
        self.dx, self.dy = 1, -1

    def draw(self):
        self.game.screen.blit(self.image, self.ball)

    def move(self):
        self.ball.x += self.speed * self.dx
        self.ball.y += self.speed * self.dy

    def check_collisions(self):
        if self.ball.centerx < self.radius or self.ball.centerx > self.game.WIDTH - self.radius:
            self.dx = -self.dx
        if self.ball.centery < self.radius:
            self.dy = -self.dy

    def calculate_movement(self, rect):
        if self.dx > 0:
            delta_x = self.ball.right - rect.left
        else:
            delta_x = rect.right - self.ball.left

        if self.dy > 0:
            delta_y = self.ball.bottom - rect.top
        else:
            delta_y = rect.bottom - self.ball.top

        if abs(delta_x - delta_y) < 10:
            self.dx, self.dy = -self.dx, -self.dy

        elif delta_x > delta_y:
            self.dy = -self.dy

        elif delta_x < delta_y:
            self.dx = -self.dx

    def check_paddle(self):
        if self.ball.colliderect(self.game.paddle) and self.dy > 0:
            self.calculate_movement(self.game.paddle.rect)

    def check_block_collision(self):
        hit_index = self.ball.collideobjects(self.game.block_list)

        if hit_index:
            print(self.game.block_list)
            self.calculate_movement(hit_index.rect)
            self.game.FPS += 2
            self.game.block_list.remove(hit_index)

    def update(self):
        self.move()
        self.check_collisions()
        self.check_paddle()
        self.check_block_collision()
