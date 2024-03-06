import pygame
import sys
import random

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 700

GRIDSIZE = 35
GRID_WIDTH = SCREEN_WIDTH // GRIDSIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRIDSIZE

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

class Snake:
    def __init__(self):
        self.length = 1
        self.positions = [((SCREEN_WIDTH // 2), (SCREEN_HEIGHT // 2))]
        self.direction = None
        self.color = (0, 255, 0)

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
        self.direction = None

    def draw(self, surface):
        for p in self.positions:
            pygame.draw.rect(surface, self.color, (p[0], p[1], GRIDSIZE, GRIDSIZE))

class Food:
    def __init__(self):
        self.position = (0, 0)
        self.color = (255, 0, 0)
        self.randomize_position()

    def randomize_position(self):
        self.position = (random.randint(0, GRID_WIDTH-1)*GRIDSIZE, random.randint(0, GRID_HEIGHT-1)*GRIDSIZE)

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.position[0], self.position[1], GRIDSIZE, GRIDSIZE))

class StartMenu:
    def __init__(self):
        self.selected_level = None
        self.levels = ["Easy", "Medium", "Hard"]
        self.level_difficulties = {
            "Easy": {"speed": 10, "grid_size": 35},
            "Medium": {"speed": 15, "grid_size": 25},
            "Hard": {"speed": 20, "grid_size": 20}
        }
        self.font = pygame.font.Font(None, 36)
        self.text_color = (255, 255, 255)
        self.selected_color = (255, 0, 0)
        self.menu_position = (100, 100)
        self.menu_spacing = 50

    def draw_menu(self, surface):
        for i, level in enumerate(self.levels):
            text = self.font.render(level, True, self.text_color if i != self.selected_level else self.selected_color)
            text_rect = text.get_rect(center=(SCREEN_WIDTH//2, self.menu_position[1] + i*self.menu_spacing))
            surface.blit(text, text_rect)

    def handle_input(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.selected_level = max(0, self.selected_level - 1)
            elif event.key == pygame.K_DOWN:
                self.selected_level = min(len(self.levels) - 1, self.selected_level + 1)
            elif event.key == pygame.K_RETURN:
                return self.selected_level
        return None

class GameOverMenu:
    def __init__(self):
        self.font = pygame.font.Font(None, 36)
        self.text_color = (255, 255, 255)
        self.menu_position = (100, 100)
        self.menu_spacing = 50
        self.options = ["Restart", "Quit"]
        self.selected_option = 0

    def draw_menu(self, surface):
        for i, option in enumerate(self.options):
            text = self.font.render(option, True, self.text_color if i != self.selected_option else (255, 0, 0))
            text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, self.menu_position[1] + i * self.menu_spacing))
            surface.blit(text, text_rect)

    def handle_input(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.selected_option = (self.selected_option - 1) % len(self.options)
            elif event.key == pygame.K_DOWN:
                self.selected_option = (self.selected_option + 1) % len(self.options)
            elif event.key == pygame.K_RETURN:
                return self.selected_option
        return None

def game_over():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)

    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()

    game_over_menu = GameOverMenu()
    is_game_over = True

    while is_game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        selected_option = game_over_menu.handle_input(pygame.event.Event(pygame.KEYDOWN, {}))
        if selected_option is not None:
            if selected_option == 0:  # Restart option selected
                return True  # Start a new game
            elif selected_option == 1:  # Quit option selected
                pygame.quit()
                sys.exit()

        surface.fill((0, 0, 0))
        game_over_menu.draw_menu(surface)
        screen.blit(surface, (0, 0))
        pygame.display.update()
        clock.tick(10)

def start_game(selected_level, difficulty):
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)

    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()

    snake = Snake()
    food = Food()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake.turn(UP)
                elif event.key == pygame.K_DOWN:
                    snake.turn(DOWN)
                elif event.key == pygame.K_LEFT:
                    snake.turn(LEFT)
                elif event.key == pygame.K_RIGHT:
                    snake.turn(RIGHT)

        snake.move()

        if snake.get_head_position() == food.position:
            snake.length += 1
            food.randomize_position()

        drawGrid(surface)
        snake.draw(surface)
        food.draw(surface)
        screen.blit
