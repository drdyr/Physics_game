import pygame
import sys
import math

pygame.init()

arrow_img = pygame.image.load("./assets/arrow.png")


class Arrow:
    def __init__(self, x, y, u, angle):
        self.u = u
        self.angle = angle
        self.x = x
        self.y = y
        self.t = 0
        self.image = pygame.image.load("./assets/arrow.png")
        self.rect = self.image.get_rect(center=(self.x, self.y))
        self.horizontal_u = math.cos(self.angle) * self.u
        self.vertical_u = math.sin(self.angle) * self.u


    def flight_angle(self):
        vertical_v = self.vertical_u - 9.81 * self.t
        flight_angle = math.atan(vertical_v / self.horizontal_u)
        flight_angle *= 180 / math.pi
        return round(flight_angle, 2)

    def draw(self):
        self.rot_center(10)
        rect = self.image.get_rect(center=(self.x, self.y))
        screen.blit(self.image, rect)

    def update(self):
        vertical_v = self.vertical_u - 9.81 * self.t
        print(self.flight_angle())
        self.t += 1/6
        self.x += 1/6 * self.horizontal_u
        self.y -= 1/6 * vertical_v - 0.5 * 9.81 * (1/6) ** 2

    def rot_center(self, angle):
        center = self.rect.center
        self.image = pygame.transform.rotate(self.image, angle)
        self.rect = self.image.get_rect(center=(self.x, self.y))


screen_width, screen_height = 1600, 800
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

arrow = Arrow(10, 500, 50, math.pi/2.5)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                arrow.rot_center(45)

    screen.fill((0, 0, 0))
    arrow.draw()
    arrow.update()

    pygame.display.flip()
    clock.tick(6)
