import pygame
import math
from pygame.draw import *
from random import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((536, 758))


def hedgedog(x, y, size):
    ellipse(screen, (63, 62, 57), (x, y, 210 * size, 100 * size))
    ellipse(screen, (63, 62, 57), (x + 160 * size, y + 80 * size, 30 * size, 20 * size))
    ellipse(screen, (63, 62, 57), (x + 180 * size, y + 65 * size, 30 * size, 20 * size))
    ellipse(screen, (63, 62, 57), (x - 10 * size, y + 65 * size, 30 * size, 20 * size))
    ellipse(screen, (63, 62, 57), (x + 10 * size, y + 80 * size, 30 * size, 20 * size))

    for i in range(570):
        X = randint(x, x + 160 * size)
        Y = randint(y, y + 100 * size)
        A = randint(-20, 20)
        if ((X - x - 105 * size) / 105 * size) ** 2 + ((Y - y - 60 * size) / 50 * size) ** 2 < 1:
            polygon(screen, (36, 32, 23),
                    [(X, Y), (X + 15 * size * math.cos(A / 180 * math.pi), Y - 15 * size + math.sin(A / 180 * math.pi)),
                     (
                         X - 70 * size * math.cos(math.atan(20 / 3) + A / 180 * math.pi),
                         Y - 70 * size * math.sin(math.atan(20 / 3) + A / 180 * math.pi))])
    ellipse(screen, (63, 62, 57), (x + 185 * size, y + 35 * size, 80 * size, 50 * size))
    circle(screen, (0, 0, 0), (x + 262 * size, y + 55 * size), 5 * size)
    circle(screen, (0, 0, 0), (x + 215 * size, y + 50 * size), 8 * size)
    circle(screen, (0, 0, 0), (x + 235 * size, y + 40 * size), 8 * size)


rect(screen, (105, 85, 55), (0, 540, 794, 228))
rect(screen, (38, 179, 36), (0, 0, 794, 540))
hedgedog(170, 520, 0.5)
rect(screen, (240, 191, 70), (0, 0, 70, 590))
rect(screen, (240, 191, 70), (100, 0, 130, 748))
rect(screen, (240, 191, 70), (326, 0, 80, 590))
rect(screen, (240, 191, 70), (466, 0, 60, 630))

hedgedog(270, 630, 1)
hedgedog(-30, 600, 0.5)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()