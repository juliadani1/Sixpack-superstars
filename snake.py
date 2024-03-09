import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, GRIDSIZE

class Snake:
    # Ormen initaliseras med längd, position, startriktning och färg
    def __init__(self):
        self.length = 1
        self.positions = [((SCREEN_WIDTH // 2), (SCREEN_HEIGHT // 2))]
        self.direction = None  
        self.color = (160, 32, 240)

    # Returnerar ormens startposition
    def initialisera_plats(self):
        return self.positions[0]

    # Ändrar ormens riktning
    def sväng(self, point):
        if self.length > 1 and (point[0]*-1, point[1]*-1) == self.direction:
            return
        else:
            self.direction = point

    # Kontrollerar när orm är utanför spelplan eller slår in i sig själv och isf startar om spel
    def rörelse(self):
        if self.direction is not None:
            cur = self.initialisera_plats()
            x, y = self.direction
            new = (cur[0]+(x*GRIDSIZE), cur[1]+(y*GRIDSIZE))

            if new[0] < 0 or new[0] >= SCREEN_WIDTH or new[1] < 0 or new[1] >= SCREEN_HEIGHT:
                self.omstart()
            elif len(self.positions) > 2 and new in self.positions[2:]:
                self.omstart()
            else:
                self.positions.insert(0, new)
                if len(self.positions) > self.length:
                    self.positions.pop()

    # Startar om spelet
    def omstart(self):
        self.length = 1
        self.positions = [((SCREEN_WIDTH // 2), (SCREEN_HEIGHT // 2))]
        self.direction = None  # Change this line

    # Ritar upp ormen
    def draw(self, surface):
        for p in self.positions:
            pygame.draw.rect(surface, self.color, (p[0], p[1], GRIDSIZE, GRIDSIZE))
