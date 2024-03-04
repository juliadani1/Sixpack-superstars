import pygame
import sys
import random



class Food:
    def __init__(self):
        self.position = (0, 0)
        self.color = (255, 0, 0)
        self.randomize_position()

    def randomize_position(self):
        self.position = (random.randint(0, GRID_WIDTH-1)*GRIDSIZE, random.randint(0, GRID_HEIGHT-1)*GRIDSIZE)

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.position[0], self.position[1], GRIDSIZE, GRIDSIZE))

def drawGrid(surface):
    for y in range(0, int(GRID_HEIGHT)):
        for x in range(0, int(GRID_WIDTH)):
            if (x+y)%2 == 0:
                r = pygame.Rect((x*GRIDSIZE, y*GRIDSIZE, GRIDSIZE, GRIDSIZE))
                pygame.draw.rect(surface, (93, 216, 228), r)
            else:
                rr = pygame.Rect((x*GRIDSIZE, y*GRIDSIZE, GRIDSIZE, GRIDSIZE))
                pygame.draw.rect(surface, (84, 194, 205), rr)


From Constants.py import SCREEN_WIDTH, SCREEN_HEIGHT, GRIDSIZE, UP, DOWN, LEFT, RIGHT 

def main():
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
        screen.blit(surface, (0,0))
        pygame.display.update()
        clock.tick(12)

if __name__ == "__main__":
    main()
