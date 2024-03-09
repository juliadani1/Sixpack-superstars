import pygame
import random
from constants import GRID_WIDTH, GRID_HEIGHT, GRIDSIZE

class Food:
    # Skapar maten
    def __init__(self):
        self.position = (0, 0)
        self.color = (220, 20, 60) 
        self.random_plats()

    # Slumpar en plats för maten på skärmen
    def random_plats(self):
        self.position = (random.randint(0, GRID_WIDTH-1)*GRIDSIZE, random.randint(0, GRID_HEIGHT-1)*GRIDSIZE)

    # Ritar upp maten på skärmen
    def måla(self, surface):
        pygame.draw.rect(surface, self.color, (self.position[0], self.position[1], GRIDSIZE, GRIDSIZE))
