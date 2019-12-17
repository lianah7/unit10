# by Liana Hill
# last modified December 17, 2019
# unit 10 option three project


import pygame, sys
from pygame.locals import *

pygame.init()
main_surface = pygame.display.set_mode((500, 500), 0, 32)
pygame.display.set_caption("Target")
main_surface.fill((255, 255, 255))


def draw_target():
    pygame.draw.circle(main_surface, (255, 255, 255), (250, 250), 20, 1)


def main():
    draw_target()


main()


while True:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()





main()