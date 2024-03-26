from random import randrange

import pygame as pg


class Ball:
    def __init__(self, root):
        self.game = root
        self.radius = 10
        self.speed = 5

        self.rect = int(self.radius * 2 ** 0.5)

        self.ball = pg.Rect(randrange(self.rect, self.game.WIDTH - self.rect),
                            self.game.HEIGHT // 2, self.rect, self.rect)
        self.dx, self.dy = 1, -1

    def draw(self):
        pg.draw.circle(self.game.screen,
                       pg.Color(255, 255, 255),
                       self.ball.center,
                       self.radius)

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
        hit_index = self.ball.collidelist(self.game.block_list)

        if hit_index != -1:
            hit_rect = self.game.block_list.pop(hit_index)
            self.game.color_list.pop(hit_index)
            self.calculate_movement(hit_rect)
            self.game.FPS += 2

    def update(self):
        self.move()
        self.check_collisions()
        self.check_paddle()
        self.check_block_collision()
