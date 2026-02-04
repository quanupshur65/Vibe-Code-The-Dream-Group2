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
import pygame
import sys

# --- Models ---

class Player:
    def __init__(self, name, position, stats=None, injured=False):
        self.name = name
        self.position = position
        self.stats = stats if stats else {}
        self.injured = injured

    def __str__(self):
        return f"{self.name} ({self.position}) - {'Injured' if self.injured else 'Healthy'}"

class Team:
    def __init__(self, name):
        self.name = name
        self.players = []

    def add_player(self, p):
        self.players.append(p)

    def remove_player(self, name):
        self.players = [p for p in self.players if p.name != name]

    def get_players(self):
        return self.players

class Game:
    def __init__(self, opponent, date):
        self.opponent = opponent
        self.date = date

# --- Sample Data ---

basketball = Team("Albright Basketball")
basketball.add_player(Player("Joey Callahan", "G", {"points": 12}, injured=False))
basketball.add_player(Player("Jeremiah Stanton", "G", {"points": 10}, injured=False))
basketball.add_player(Player("Qadir Mitchell", "G", {"points": 8}, injured=True))
basketball.add_player(Player("Miles Smith", "G", {"points": 7}))
basketball.add_player(Player("Akhir Keys", "G", {"points": 5}))

football = Team("Albright Football")
football.add_player(Player("Alden Stickler", "WR", {"receptions": 15}, False))
football.add_player(Player("Matthew Creeger", "WR", {"receptions": 12}))
football.add_player(Player("Logan Rothberg", "WR", {"yards": 250}))
football.add_player(Player("Darien Osmun", "LB", {"tackles": 32}))
football.add_player(Player("Daniel Farley", "P", {"punts": 18}))

schedule = [
    Game("Misericordia", "Sep 13"),
    Game("Widener", "Sep 27"),
    Game("FDU-Florham", "Oct 25")
]

# --- Pygame UI Setup ---

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Albright Sports Team Manager")
font = pygame.font.SysFont(None, 28)

current_team = basketball  # toggle between basketball / football

def draw_text(surface, text, x, y, color=(255, 255, 255)):
    txt = font.render(text, True, color)
    surface.blit(txt, (x, y))

def draw_menu():
    screen.fill((25, 25, 51))
    draw_text(screen, f"Team: {current_team.name}", 50, 20)

    y = 60
    for p in current_team.get_players():
        draw_text(screen, f"- {p}", 50, y)
        y += 30

    draw_text(screen, "Schedule:", 50, 300)
    y_sched = 340
    for g in schedule:
        draw_text(screen, f"{g.date} vs {g.opponent}", 70, y_sched)
        y_sched += 25

    draw_text(screen, "[TAB] Switch Team  [A] Add Player  [R] Remove Player", 50, 500)
    pygame.display.flip()

def add_player():
    current_team.add_player(Player("New Player", "Pos"))

def remove_player():
    if current_team.players:
        current_team.remove_player(current_team.players[-1].name)

# --- Loop ---

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_TAB:
                current_team = football if current_team == basketball else basketball
            if event.key == pygame.K_a:
                add_player()
            if event.key == pygame.K_r:
                remove_player()

    draw_menu()
    clock.tick(30)

pygame.quit()
sys.exit()
