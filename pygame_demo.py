import pygame, sys
from pygame.locals import *

pygame.init()

main_surface = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption("Pygame Demo - So Cool")
main_surface.fill((255, 255, 255))

pygame.draw.rect(main_surface, (0, 0, 255), (50, 50, 200, 100), 0)
pygame.draw.circle(main_surface, (123, 111, 222), (250, 250), 100, 5)
pygame.draw.polygon(main_surface, (23, 100, 25), ((25, 100), (100, 250), (400, 300)), 0)
pygame.draw.line(main_surface, (100, 100, 100), (200, 200), (45, 10), 3)
pygame.draw.ellipse(main_surface, (255, 10, 10), (50, 50, 200, 100), 0)


while True:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()