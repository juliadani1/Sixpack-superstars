import pygame
import random
from constants import GRID_WIDTH, GRID_HEIGHT, GRIDSIZE

class Food:
    def __init__(self):
        self.position = (0, 0)
        self.color = (220, 20, 60) 
        self.randomize_position()

    def randomize_position(self):
        self.position = (random.randint(0, GRID_WIDTH-1)*GRIDSIZE, random.randint(0, GRID_HEIGHT-1)*GRIDSIZE)

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.position[0], self.position[1], GRIDSIZE, GRIDSIZE))
