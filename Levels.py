import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, GRID_SIZE

class Levels:
    def __init__(self):
        self.selected_level = None
        self.levels = ["Easy", "Medium", "Hard"]
        self.level_difficulties = {
            "Easy": {"speed": 10, "grid_size": 35, "background": "grass.png"},
            "Medium": {"speed": 15, "grid_size": 25, "background": "rocks.png"},
            "Hard": {"speed": 20, "grid_size": 20, "background": "space.png"}
        }
        self.font = pygame.font.Font(None, 36)
        self.text_color = (0, 0, 255)
        self.selected_color = (0, 0, 128)
        self.menu_position = (100, 100)
        self.menu_spacing = 50
        
