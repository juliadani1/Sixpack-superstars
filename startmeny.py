import pygame
import sys
 
def display_menu():
    pygame.init()

    screen = pygame.display.set_mode((700, 700))
    font = pygame.font.Font(None, 36)

    button1 = pygame.Rect(50, 100, 200, 50)  # x, y, width, height
    button2 = pygame.Rect(50, 200, 200, 50)
    button3 = pygame.Rect(50, 300, 200, 50)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos  # gets mouse position

                # checks if mouse position is over the button
                if button1.collidepoint(mouse_pos):
                    return 1
                elif button2.collidepoint(mouse_pos):
                    return 2
                elif button3.collidepoint(mouse_pos):
                    return 3

        screen.fill((0, 0, 255))

        pygame.draw.rect(screen, [253, 253, 150], button1)  # draw button
        pygame.draw.rect(screen, [237, 110, 0], button2)  # draw button
        pygame.draw.rect(screen, [210, 1, 23], button3)  # draw button

        text1 = font.render('Level 1', True, (0, 0, 0))
        screen.blit(text1, (50, 100))

        text2 = font.render('Level 2', True, (0, 0, 0))
        screen.blit(text2, (50, 200))

        text3 = font.render('Level 3', True, (0, 0, 0))
        screen.blit(text3, (50, 300))

        pygame.display.flip()
    

level = display_menu()
