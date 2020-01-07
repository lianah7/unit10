import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)


class Target:

    def __init__(self, main_surface):
        self.main_surface = main_surface
        self.score = 0

    def draw_target(self, p):
        """
        thsi function draws the target circle
        :param p: position of the circles
        :return: nothing
        """
        c = p[0]
        a = p[1]
        b = p[2]
        pygame.draw.circle(self.main_surface, c, (250, 250), a, b)

    def get_score(self, position):
        """
        this function gives a score to the user depending on what color they hit
        :param position: position of where the use clicks
        :return: nothing
        """
        target_color = self.main_surface.get_at(position)
        if target_color == (255, 255, 255, 255):
            self.update_score(1)
        if target_color == (0, 0, 0, 255):
            self.update_score(3)
        if target_color == (0, 0, 255, 255):
            self.update_score(5)
        if target_color == (255, 0, 0, 255):
            self.update_score(7)
        if target_color == (255, 255, 0, 255):
            self.update_score(9)

    def update_score(self, score):
        """
        this function shows the user their score after every click
        :param score: the user's score
        :return: nothing
        """
        self.main_surface.fill((255, 255, 255))
        circles = [(BLACK, 202, 1), (WHITE, 200, 1), (BLACK, 160, 0), (BLUE, 120, 0), (RED, 80, 0), (YELLOW, 40, 0)]
        for x in circles:
            self.draw_target(x)
        self.score += score
        mouse_font = pygame.font.SysFont("Helvetica", 32)
        mouse_label = mouse_font.render(str(self.score), 1, (0, 0, 0))
        self.main_surface.blit(mouse_label, (30, 30))
        pygame.display.update()

