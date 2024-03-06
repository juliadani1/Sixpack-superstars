class GameOverMenu:
    def __init__(self, score):
        self.score = score
        self.font = pygame.font.Font(None, 48)
        self.text_color = (255, 255, 255)
        self.menu_font = pygame.font.Font(None, 36)
        self.menu_position = (100, 200)
        self.menu_spacing = 50
        self.options = ["Restart", "Quit"]
        self.selected_option = 0

    def draw_menu(self, surface):
        game_over_text = self.font.render("GAME OVER", True, self.text_color)
        game_over_rect = game_over_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50))
        surface.blit(game_over_text, game_over_rect)

        score_text = self.font.render("Score: " + str(self.score), True, self.text_color)
        score_rect = score_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        surface.blit(score_text, score_rect)

        for i, option in enumerate(self.options):
            text = self.menu_font.render(option, True, self.text_color if i != self.selected_option else (255, 0, 0))
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

def game_over(score):
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)

    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()

    game_over_menu = GameOverMenu(score)
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
