import pygame
import sys
 
def visa_meny():
    pygame.init()

    screen = pygame.display.set_mode((700, 700))
    font = pygame.font.Font(None, 36)

    knapp1 = pygame.Rect(250, 100, 200, 50)  # x, y, width, height
    knapp2 = pygame.Rect(250, 200, 200, 50)
    knapp3 = pygame.Rect(250, 300, 200, 50)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos  # gets mouse position

                # checks if mouse position is over the button
                if knapp1.collidepoint(mouse_pos):
                    return 1
                elif knapp2.collidepoint(mouse_pos):
                    return 2
                elif knapp3.collidepoint(mouse_pos):
                    return 3

        screen.fill((183, 225, 238))

        pygame.draw.rect(screen, [253, 253, 150], knapp1)  # draw button
        pygame.draw.rect(screen, [237, 110, 0], knapp2)  # draw button
        pygame.draw.rect(screen, [210, 1, 23], knapp3)  # draw button

        text1 = font.render('Level 1', True, (0, 0, 0))
        screen.blit(text1, (300, 110))

        text2 = font.render('Level 2', True, (0, 0, 0))
        screen.blit(text2, (300, 210))

        text3 = font.render('Level 3', True, (0, 0, 0))
        screen.blit(text3, (300, 310))

        pygame.display.flip()
    
