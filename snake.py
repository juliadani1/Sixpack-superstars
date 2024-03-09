import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, GRIDSIZE

class Snake:
    def __init__(self):
        self.length = 1
        self.positions = [((SCREEN_WIDTH // 2), (SCREEN_HEIGHT // 2))]
        self.direction = None  
        self.color = (160, 32, 240)

    def get_head_position(self):
        return self.positions[0]

    def turn(self, point):
        if self.length > 1 and (point[0]*-1, point[1]*-1) == self.direction:
            return
        else:
            self.direction = point

    def move(self):
        if self.direction is not None:
            cur = self.get_head_position()
            x, y = self.direction
            new = (cur[0]+(x*GRIDSIZE), cur[1]+(y*GRIDSIZE))

            # Check if the new position is outside the screen boundaries
            if new[0] < 0 or new[0] >= SCREEN_WIDTH or new[1] < 0 or new[1] >= SCREEN_HEIGHT:
                self.reset()
            elif len(self.positions) > 2 and new in self.positions[2:]:
                self.reset()
            else:
                self.positions.insert(0, new)
                if len(self.positions) > self.length:
                    self.positions.pop()

    def reset(self):
        self.length = 1
        self.positions = [((SCREEN_WIDTH // 2), (SCREEN_HEIGHT // 2))]
        self.direction = None  # Change this line

    def draw(self, surface):
        for p in self.positions:
            pygame.draw.rect(surface, self.color, (p[0], p[1], GRIDSIZE, GRIDSIZE))
