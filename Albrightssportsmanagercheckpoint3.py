import pygame
import sys

# ---------- Models ----------

class Player:
    def __init__(self, name, position, stats=None, injured=False):
        self.name = name
        self.position = position
        self.stats = stats if stats else {}
        self.injured = injured

    def toggle_injury(self):
        self.injured = not self.injured

    def status(self):
        return "Injured" if self.injured else "Healthy"


class Team:
    def __init__(self, name, team_stats=None):
        self.name = name
        self.players = []
        self.team_stats = team_stats if team_stats else {}

    def add_player(self, p):
        self.players.append(p)


class Game:
    def __init__(self, opponent, date):
        self.opponent = opponent
        self.date = date


# ---------- Data ----------

basketball = Team(
    "Albright Basketball",
    team_stats={"PPG": 74, "Record": "14-11", "Conference": "MAC"}
)

basketball.players = [
    Player("Joey Callahan", "G", {"Points": 12, "Assists": 4}),
    Player("Jeremiah Stanton", "G", {"Points": 10, "Assists": 3}),
    Player("Qadir Mitchell", "G", {"Points": 8}, injured=True),
    Player("Miles Smith", "G", {"Points": 7}),
    Player("Akhir Keys", "G", {"Points": 5}),
]

basketball_schedule = [
    Game("Penn St. Berks", "Nov 7"),
    Game("Ursinus", "Nov 11"),
    Game("Saint Joseph (CT)", "Nov 15"),
    Game("Farmingdale State", "Nov 16"),
    Game("Franklin and Marshall", "Nov 20"),
    Game("Swarthmore", "Nov 25"),
    Game("Lebanon Valley", "Dec 3"),
    Game("Stevens", "Dec 6"),
    Game("Kean", "Dec 16"),
    Game("Pitt-Greensburg", "Dec 29"),
    Game("Stockton", "Dec 30"),
    Game("Hood", "Jan 7"),
    Game("Eastern", "Jan 10"),
    Game("Messiah", "Jan 14"),
    Game("Alvernia", "Jan 17"),
    Game("Widener", "Jan 21"),
    Game("York", "Jan 24"),
    Game("Stevenson", "Jan 29"),
    Game("Eastern", "Jan 31"),
    Game("Messiah", "Feb 4"),
    Game("Alvernia", "Feb 7"),
    Game("Widener", "Feb 11"),
    Game("Hood", "Feb 14"),

]

football = Team(
    "Albright Football",
    team_stats={"Record": "5-5", "Points/Game": 28, "Conference": "MAC"}
)

football.players = [
    Player("Alden Stickler", "WR", {"Receptions": 15, "Yards": 220}),
    Player("Matthew Creeger", "WR", {"Receptions": 12, "Yards": 180}),
    Player("Logan Rothberg", "WR", {"Yards": 250}),
    Player("Darien Osmun", "LB", {"Tackles": 32}),
    Player("Daniel Farley", "P", {"Punts": 18}),
]

football_schedule = [
    Game("Gallaudet", "Sep 5"),           
    Game("Misericordia", "Sep 13"),      
    Game("Delaware Valley", "Sep 20"),    
    Game("Widener", "Sep 27"),           
    Game("Alvernia", "Oct 11"),           
    Game("Eastern", "Oct 18"),            
    Game("FDU-Florham", "Oct 25"),        
    Game("King's", "Nov 1"),             
    Game("Stevenson", "Nov 8"),           
    Game("Lebanon Valley", "Nov 15")      
]

# ---------- Pygame Setup ----------

pygame.init()
screen = pygame.display.set_mode((900, 650))
pygame.display.set_caption("Albright Sports Team Manager")
font = pygame.font.SysFont(None, 26)

current_team = basketball
current_schedule = basketball_schedule
selected_index = 0
show_stats = False

# ---------- Helpers ----------

def draw_text(text, x, y, color=(255, 255, 255)):
    screen.blit(font.render(text, True, color), (x, y))


def draw_menu():
    screen.fill((20, 20, 45))

    draw_text(f"Team: {current_team.name}", 40, 20)

    # Team stats
    y = 55
    for k, v in current_team.team_stats.items():
        draw_text(f"{k}: {v}", 40, y, (180, 180, 255))
        y += 22

    # Players
    y = 140
    for i, p in enumerate(current_team.players):
        color = (255, 255, 0) if i == selected_index else (255, 255, 255)
        draw_text(
            f"{p.name} ({p.position}) - {p.status()}",
            40, y, color
        )
        y += 28

    # Schedule
    draw_text("Schedule:", 450, 20)
    y = 55
    for g in current_schedule:
        draw_text(f"{g.date} vs {g.opponent}", 450, y)
        y += 24

    # Player stats panel
    if show_stats:
        p = current_team.players[selected_index]
        draw_text("Player Stats:", 450, 300, (0, 255, 200))
        y = 330
        for k, v in p.stats.items():
            draw_text(f"{k}: {v}", 450, y)
            y += 24

    draw_text(
        "[TAB] Switch Team  [↑↓] Select Player  [A] Toggle Injury  [R] Show Stats",
        40, 610
    )

    pygame.display.flip()


# ---------- Main Loop ----------

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_TAB:
                if current_team == basketball:
                    current_team = football
                    current_schedule = football_schedule
                else:
                    current_team = basketball
                    current_schedule = basketball_schedule
                selected_index = 0
                show_stats = False

            elif event.key == pygame.K_UP:
                selected_index = max(0, selected_index - 1)

            elif event.key == pygame.K_DOWN:
                selected_index = min(
                    len(current_team.players) - 1,
                    selected_index + 1
                )

            elif event.key == pygame.K_a:
                current_team.players[selected_index].toggle_injury()

            elif event.key == pygame.K_r:
                show_stats = not show_stats

    draw_menu()
    clock.tick(30)

pygame.quit()
sys.exit()

