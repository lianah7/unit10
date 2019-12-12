# by Liana Hill
# last modified December 12, 2019
# daily exercise picture recreation

import pygame, sys
from pygame.locals import *

main_surface = pygame.display.set_mode((500, 500), 0, 32)
pygame.display.set_caption("Night Sky Picture")
main_surface.fill((16, 78, 139))

pygame.draw.circle(main_surface, (209, 209, 209), (90, 110), 50, 0)

def make_star():

pygame.draw.circle(main_surface, (229, 229, 229), (175, 200), 3, 0)


while True:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
