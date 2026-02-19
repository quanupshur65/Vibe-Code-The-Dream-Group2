import pygame
import sys



class Player:
    def __init__(self, name, position, number, stats=None, injured=False):
        self.name = name
        self.position = position
        self.number = number
        self.stats = stats if stats else {}
        self.injured = injured

    def toggle_injury(self):
        self.injured = not self.injured

    def status(self):
        return "Injured" if self.injured else "Healthy"


class Team:
    def __init__(self, name, team_stats=None, summary=""):
        self.name = name
        self.players = []
        self.team_stats = team_stats if team_stats else {}
        self.summary = summary


class Game:
    def __init__(self, opponent, date):
        self.opponent = opponent
        self.date = date



basketball = Team(
    "Albright Basketball",
    {"PPG": 74, "Record": "14-11", "Conference": "MAC"},
    "Albright Basketball is a competitive MAC program known for strong guard play and balanced scoring."
)

basketball.players = [
    Player("Joey Callahan", "G", 0),
    Player("Jeremiah Stanton", "G", 1),
    Player("Qadir Mitchell", "G", 2, injured=True),
    Player("Miles Smith", "G", 3),
    Player("Akhir Keys", "G", 4),
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
    {"Record": "5-5", "Points/Game": 28, "Conference": "MAC"},
    "Albright Football competes in the MAC conference with a balanced offense and aggressive defense."
)

football.players = [
    Player("Alden Stickler", "WR", 1),
    Player("Matthew Creeger", "WR", 3),
    Player("Logan Rothberg", "WR", 9),
    Player("Darien Osmun", "LB", 6),
    Player("Daniel Farley", "P", 10),
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
    Game("Lebanon Valley", "Nov 15"),
]


pygame.init()
screen = pygame.display.set_mode((900, 650))
pygame.display.set_caption("Albright Sports Team Manager")
font = pygame.font.SysFont(None, 24)

current_team = basketball
current_schedule = basketball_schedule
selected_index = 0

editing = False
adding = False
edit_step = 0
input_text = ""
fields = ["Name", "Number", "Position", "Injured (yes/no)"]


def draw_text(text, x, y, color=(255, 255, 255)):
    screen.blit(font.render(text, True, color), (x, y))


def draw_wrapped_text(text, x, y, max_width):
    words = text.split(" ")
    line = ""
    for word in words:
        test = line + word + " "
        if font.size(test)[0] < max_width:
            line = test
        else:
            draw_text(line, x, y)
            y += 22
            line = word + " "
    draw_text(line, x, y)
    return y + 25


def draw_menu():
    screen.fill((20, 20, 45))

    draw_text(f"Team: {current_team.name}", 40, 20, (255, 255, 0))

    y = 55
    for k, v in current_team.team_stats.items():
        draw_text(f"{k}: {v}", 40, y, (180, 180, 255))
        y += 22

    y += 10
    draw_text("Team Summary:", 40, y, (0, 255, 200))
    y = draw_wrapped_text(current_team.summary, 40, y + 25, 400)

    y += 10
    draw_text("Players:", 40, y, (255, 200, 0))
    y += 30

    for i, p in enumerate(current_team.players):
        color = (255, 255, 0) if i == selected_index else (255, 255, 255)
        draw_text(f"#{p.number} {p.name} ({p.position}) - {p.status()}", 40, y, color)
        y += 25

    draw_text("Schedule:", 500, 20, (0, 255, 200))
    sy = 55
    for g in current_schedule:
        draw_text(f"{g.date} vs {g.opponent}", 500, sy)
        sy += 22
        if sy > 620:
            break

    if editing or adding:
        pygame.draw.rect(screen, (50, 50, 80), (150, 500, 600, 80))
        mode = "Editing Player" if editing else "Adding Player"
        draw_text(f"{mode} - Enter {fields[edit_step]}:", 160, 510)
        draw_text(input_text, 160, 540)

    draw_text(
        "[TAB] Switch  [↑↓] Select  [A] Toggle Injury  [E] Edit Player  [D] Add Player",
        40, 620
    )

    pygame.display.flip()


def handle_edit_input(player):
    global edit_step, editing, input_text

    if edit_step == 0:
        player.name = input_text
    elif edit_step == 1 and input_text.isdigit():
        player.number = int(input_text)
    elif edit_step == 2:
        player.position = input_text
    elif edit_step == 3:
        player.injured = input_text.lower() == "yes"

    edit_step += 1
    input_text = ""

    if edit_step >= len(fields):
        editing = False
        edit_step = 0


def handle_add_input():
    global edit_step, adding, input_text, new_player_data

    if edit_step == 0:
        new_player_data["name"] = input_text
    elif edit_step == 1:
        new_player_data["number"] = int(input_text) if input_text.isdigit() else 0
    elif edit_step == 2:
        new_player_data["position"] = input_text
    elif edit_step == 3:
        injured = input_text.lower() == "yes"
        current_team.players.append(
            Player(
                new_player_data["name"],
                new_player_data["position"],
                new_player_data["number"],
                {},
                injured
            )
        )

    edit_step += 1
    input_text = ""

    if edit_step >= len(fields):
        adding = False
        edit_step = 0



clock = pygame.time.Clock()
running = True
new_player_data = {}

while running:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if editing:
                if event.key == pygame.K_RETURN:
                    handle_edit_input(current_team.players[selected_index])
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                elif event.key == pygame.K_ESCAPE:
                    editing = False
                    edit_step = 0
                    input_text = ""
                else:
                    input_text += event.unicode
                continue

            if adding:
                if event.key == pygame.K_RETURN:
                    handle_add_input()
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                elif event.key == pygame.K_ESCAPE:
                    adding = False
                    edit_step = 0
                    input_text = ""
                else:
                    input_text += event.unicode
                continue

            if event.key == pygame.K_TAB:
                if current_team == basketball:
                    current_team = football
                    current_schedule = football_schedule
                else:
                    current_team = basketball
                    current_schedule = basketball_schedule
                selected_index = 0

            elif event.key == pygame.K_UP:
                selected_index = max(0, selected_index - 1)

            elif event.key == pygame.K_DOWN:
                selected_index = min(len(current_team.players) - 1, selected_index + 1)

            elif event.key == pygame.K_a:
                current_team.players[selected_index].toggle_injury()

            elif event.key == pygame.K_e:
                editing = True
                edit_step = 0
                input_text = ""

            elif event.key == pygame.K_d:
                adding = True
                edit_step = 0
                input_text = ""
                new_player_data = {}

    draw_menu()
    clock.tick(30)

pygame.quit()
sys.exit()
