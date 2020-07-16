import pygame
import sys
import math

pygame.init()


class Projectile():
    def __init__(self, initial_x, initial_y, initial_speed, horizontal_angle):
        self.u = initial_speed
        self.angle = horizontal_angle
        self.initial_x = initial_x
        self.initial_y = initial_y
        self.x = initial_x
        self.y = initial_y
        self.t = 0

    def draw(self):
        image = pygame.image.load("./arrow.png")
        rect = image.get_rect(center=(self.x, self.y))
        screen.blit(image, rect)

    def update(self):
        self.t += 5/60

        self.x = math.cos(self.angle) * self.u * self.t + self.initial_x  # s = ut
        self.y = -1 * (math.sin(self.angle) * self.u * self.t - 0.5 * 9.81 * self.t ** 2) + self.initial_y  # s = ut + 0.5at^2


class Cannon:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        rect = pygame.Rect(self.x, self.y, 100, 50)
        pygame.draw.rect(screen, (255, 255, 255), rect, 0)



projectile_group = []

screen_width, screen_height = 1600, 1200
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

ball = Projectile(10, 500, 50, math.pi/2.5)
cannon1 = Cannon(0, 350)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((0, 0, 0))
    ball.draw()
    ball.update()

    pygame.display.flip()
    clock.tick(60)
