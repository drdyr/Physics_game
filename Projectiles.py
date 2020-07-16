import pygame
import sys
import math

pygame.init()

arrow_img = pygame.image.load("./assets/arrow/90arrow.png")


def round_to_angle(x, angle):
    return int(round(x / angle)) * angle


class Arrow:
    def __init__(self, x, y, u, angle):
        self.u = u
        self.angle = angle
        self.x = x
        self.y = y
        self.t = 0
        self.horizontal_u = math.cos(self.angle) * self.u
        self.vertical_u = math.sin(self.angle) * self.u

    def flight_angle(self):
        vertical_v = self.vertical_u - 9.81 * self.t
        flight_angle = math.atan(vertical_v / self.horizontal_u)
        flight_angle *= 180 / math.pi
        return int(flight_angle)

    def draw(self):
        flight_angle = self.flight_angle()
        pic_angle = round_to_angle(flight_angle, 5)
        image = pygame.image.load("./assets/arrow/" + str(pic_angle) + "arrow.png")
        rect = image.get_rect(center=(self.x, self.y))
        screen.blit(image, rect)

    def update(self):
        vertical_v = self.vertical_u - 9.81 * self.t
        self.t += 1
        self.x += 1 * self.horizontal_u
        self.y -= 1 * vertical_v - 0.5 * 9.81 * (1) ** 2

    def rot_center(self, angle):
        center = self.rect.center
        self.image = pygame.transform.rotate(self.image, angle)
        self.rect = self.image.get_rect(center=(self.x, self.y))


screen_width, screen_height = 1600, 800
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

arrow = Arrow(10, 500, 100, math.pi/2.5)


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
    clock.tick(60)
