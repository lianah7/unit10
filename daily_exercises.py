# by Liana Hill
# last modified December 12, 2019
# daily exercises

import pygame, sys
from pygame.locals import *

pygame.init()

main_surface = pygame.display.set_mode((500, 500), 0, 32)
pygame.display.set_caption("Daily Exercise")
main_surface.fill((255, 255, 255))

pygame.draw.polygon(main_surface, (0, 255, 0), ((200, 50), (325, 150), (275, 300), (125, 300), (75, 150)), 0)
pygame.draw.circle(main_surface, (0, 0, 255), (330, 100), 17, 0)
pygame.draw.rect(main_surface, (255, 0, 0), (235, 185, 95, 47), 0)
pygame.draw.ellipse(main_surface, (255, 0, 0), (335, 270, 35, 75), 1)

# makes the letter "z"
pygame.draw.line(main_surface, (0, 0, 255), (130, 107), (185, 107), 3)
pygame.draw.line(main_surface, (0, 0, 255), (185, 107), (130, 155), 1)
pygame.draw.line(main_surface, (0, 0, 255), (130, 155), (185, 155), 3)

while True:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
