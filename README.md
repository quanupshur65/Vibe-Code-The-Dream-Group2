# Vibe-Code-The-Dream-Group2

Albright College Sports Team Manager
Group Members: Darwin, Quan, Kendall
Course: Computer Science Project
Technology Stack: Python, Pygame, GitHub, GitHub Copilot

Project Overview
The Albright College Sports Team Manager is a desktop application designed to help manage Albright sports teams. It will allow users to view, edit, and track basic information for college athletic teams. Users can manage players, record stats, check injury reports, view upcoming games, and generate team summaries.
This project connects to the Albright College community by focusing on campus athletics and providing a practical system for organizing team data. It also serves as a real-world exercise in data management, user interaction, and software design.

Core Features 
Core Features
Player Management: Add, edit, and remove players.
Stat Tracking: View performance stats and yearly progress.
Injury Reports: Record current injuries and recovery status.
Game Schedule: View upcoming and past matches.
Team Summaries: Display team averages and top-performing players.

System Architecture

Language: Python
Frameworks/Libraries:
pygame – for user interface display
csv or json – for lightweight data storage
os/sys – for file management
(optional) flask – for a possible web version later

Planned Classes
Player: responsibility: Represents a single player (name, position, stats, injuries).	location: models/player.py
Team: responsiblity: Contains multiple players, manages roster actions.	location: models/team.py
Game: responsibility: Tracks opponents, scores, and dates.	location:models/game.py
DataManager: responsibility: Handles saving & loading from data files.	location: services/data_manager.py
Dashboard: responsibility: Displays main interface in Pygame.	location: ui/dashboard.py

Class Interaction example

Team
 ├── players → list of Player objects
 ├── add_player(player)
 ├── remove_player(player)
 └── generate_summary()
        ↓
StatsCalculator → creates average and leaderboard info
