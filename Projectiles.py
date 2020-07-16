import pygame
import sys
import math

pygame.init()

arrow_img = pygame.image.load("./assets/arrow/90arrow.png")


def round_to_angle(x, angle):
    return int(round(x / angle)) * angle

class Powerbar:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.power = 150
        self.change = 3

    def draw(self):
        rect = pygame.Rect(self.x, self.y, self.power, 100)
        pygame.draw.rect(screen, (255, 255, 255), rect)

    def update(self):
        if self.power == 300 or self.power == 3:
            self.change *= -1
        self.power += self.change

class Arrow:
    def __init__(self, x, y, u, angle):
        self.u = u
        self.angle = angle
        self.x = x
        self.y = y
        self.t = 0
        self.horizontal_u = math.cos(self.angle) * self.u
        self.vertical_u = math.sin(self.angle) * self.u
        self.time_inc = 1/6

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
        self.t += self.time_inc
        self.x += self.time_inc * self.horizontal_u
        self.y -= self.time_inc * vertical_v - 0.5 * 9.81 * self.time_inc ** 2


screen_width, screen_height = 3000, 800
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

arrow = Arrow(0, 800, 100, math.pi/4)
powerbar = Powerbar(100, 100)

arrow_group = []

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                new_arrow = Arrow(0, 800, powerbar.power, math.pi/4)
                arrow_group.append(new_arrow)

    screen.fill((0, 0, 0))
    powerbar.draw()
    powerbar.update()
    for arrow in arrow_group:
        arrow.draw()
        arrow.update()

    pygame.display.flip()
    clock.tick(60)
