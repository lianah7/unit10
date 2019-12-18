# by Liana Hill
# last modified December 17, 2019
# unit 10 option three project


import pygame, sys
from pygame.locals import *
import target

pygame.init()
main_surface = pygame.display.set_mode((500, 500), 0, 32)
pygame.display.set_caption("Target Practice")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

main_surface.fill((255, 255, 255))
my_target = target.Target(main_surface)
circles = [(BLACK, 202, 1), (WHITE, 200, 1), (BLACK, 160, 0), (BLUE, 120, 0), (RED, 80, 0), (YELLOW, 40, 0)]
for x in circles:
    my_target.target_circle(x)


while True:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

