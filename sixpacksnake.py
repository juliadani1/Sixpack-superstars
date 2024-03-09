import pygame
import sys
import random
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, GRIDSIZE, GRID_WIDTH, GRID_HEIGHT, UP, DOWN, LEFT, RIGHT
from snake import Snake
from food import Food
from startmeny import visa_meny

# ritar upp rutnät på skärmen
def måla_rutnät(surface):
    for y in range(0, int(GRID_HEIGHT)):
        for x in range(0, int(GRID_WIDTH)):
            if (x+y)%2 == 0:
                r = pygame.Rect((x*GRIDSIZE, y*GRIDSIZE, GRIDSIZE, GRIDSIZE))
                pygame.draw.rect(surface, (235, 236, 240), r)
            else:
                rr = pygame.Rect((x*GRIDSIZE, y*GRIDSIZE, GRIDSIZE, GRIDSIZE))
                pygame.draw.rect(surface, (255, 255, 255), rr)


def main():
    # Initialiserar pygame, möjliggör reglering av hasitghet och skapar ett fönster för spelet
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()

    level = visa_meny()
    snake = Snake()
    food = Food()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake.sväng(UP)
                elif event.key == pygame.K_DOWN:
                    snake.sväng(DOWN)
                elif event.key == pygame.K_LEFT:
                    snake.sväng(LEFT)
                elif event.key == pygame.K_RIGHT:
                    snake.sväng(RIGHT)

        snake.rörelse()

        if snake.initialisera_plats() == food.position:
            snake.length += 1
            food.random_plats()

        måla_rutnät(surface)
        snake.draw(surface)
        food.draw(surface)
        screen.blit(surface, (0,0))
        pygame.display.update()
        clock.tick(10 * (level / 2))

if __name__ == "__main__":
    while True:
        
        main()  # Run the main game loop
