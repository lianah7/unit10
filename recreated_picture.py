# by Liana Hill
# last modified December 12, 2019
# daily exercise picture recreation

import pygame, sys
from pygame.locals import *
import random

main_surface = pygame.display.set_mode((500, 500), 0, 32)
pygame.display.set_caption("Night Sky Picture")
main_surface.fill((16, 78, 139))

pygame.draw.circle(main_surface, (209, 209, 209), (90, 110), 45, 0)


def make_star():
    x = random.randint(0, 500)
    y = random.randint(0, 500)
    pygame.draw.circle(main_surface, (209, 209, 209), (x, y), 3, 0)


def building(p):
    x = p[0]
    y = p[1]
    pygame.draw.rect(main_surface, (0, 0, 0), (x, y, 70, 500), 0)


def window(p):
    x = p[0]
    y = p[1]
    pygame.draw.rect(main_surface, (255, 220, 0), (x, y, 13, 13), 0)


def main():
    for x in range(80):
        make_star()
    building_points = [(0, 345), (40, 250), (100, 375), (160, 330), (210, 225), (280, 430), (330, 350), (400, 250),
                       (470, 400)]
    for x in building_points:
        building(x)
    window_points = [(55, 300), (85, 320), (55, 400), (85, 400), (420, 300), (445, 350)]
    for y in window_points:
        window(y)
    pygame.draw.ellipse(main_surface, (110, 110, 110), (120, 250, 240, 600), 23)


main()


while True:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
