import pygame

class Player:
    def __init__(self, name, position, stats=None, injured=False):
        self.name = name
        self.position = position
        self.stats = stats if stats else {}
        self.injured = injured

    def __str__(self):
        status = "Injured" if self.injured else "Healthy"
        return f"{self.name} - {self.position} ({status})"
class Team:
    def __init__(self, name):
        self.name = name
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def remove_player(self, player_name):
        self.players = [p for p in self.players if p.name != player_name]

    def get_roster(self):
        return self.players
class Game:
    def __init__(self, opponent, date):
        self.opponent = opponent
        self.date = date

    def __str__(self):
        return f"Game vs {self.opponent} on {self.date}"
class DataManager:
    def save(self, team):
        # Placeholder for future file/database saving
        pass

    def load(self):
    # Placeholder for future loading
        pass

class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.SysFont(None, 36)

    def draw(self):
        self.screen.fill((0, 0, 0))
        text = self.font.render("Albright Sports Team Manager", True, (255, 255, 255))
        self.screen.blit(text, (50, 50))
        pygame.display.flip()

def main():
    pygame.init()
    screen = pygame.display.set_mode((600, 400))
    pygame.display.set_caption("Albright Sports Team Manager")

    team = Team("Albright Lions")
    team.add_player(Player("John Smith", "Forward"))
    team.add_player(Player("Mike Johnson", "Goalie", injured=True))

    menu = Menu(screen)

    running = True
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        menu.draw()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
