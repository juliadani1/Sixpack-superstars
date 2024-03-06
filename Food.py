import pygame
import random
from constants import GRID_WIDTH, GRID_HEIGHT, GRIDSIZE

class Food:
    def __init__(self):
        self.position = (0, 0)
        self.image = pygame.image.load(Här ska directory länken ligga)
        self.image = pygame.transform.scale(self.image, (GRIDSIZE, GRIDSIZE))  # Load the image
        self.randomize_position()

    def randomize_position(self):
        self.position = (random.randint(0, GRID_WIDTH-1)*GRIDSIZE, random.randint(0, GRID_HEIGHT-1)*GRIDSIZE)

    def draw(self, surface):
        surface.blit(self.image, self.position)  # Draw the image
