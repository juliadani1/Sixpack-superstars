class StartMenu:
    def __init__(self):
        self.selected_level = None
        self.levels = ["Easy", "Medium", "Hard"]
        self.font = pygame.font.Font(None, 36)
        self.text_color = (255, 255, 255)
        self.selected_color = (253, 253, 150)
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

def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)

    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()

    start_menu = StartMenu()
    is_in_menu = True

    while is_in_menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        selected_level = start_menu.handle_input(pygame.event.Event(pygame.KEYDOWN, {}))
        if selected_level is not None:
            is_in_menu = False
            start_game(selected_level)  # Start the game with the selected level

        surface.fill((0, 0, 0))
        start_menu.draw_menu(surface)
        screen.blit(surface, (0, 0))
        pygame.display.update()
        clock.tick(10)

def start_game(selected_level):
