class Team:
    def __init__(self, name):
        self.name = name
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def display_team(self):
        print(f"Team: {self.name}")
        for player in self.players:
            print(f" - {player.name}, Role: {player.role}")

class Player:
    def __init__(self, name, role):
        self.name = name
        self.role = role
        self.runs = 0
        self.wickets = 0

    def update_performance(self, runs, wickets):
        self.runs += runs
        self.wickets += wickets

    def display_stats(self):
        print(f"Player: {self.name}, Role: {self.role}, Runs: {self.runs}, Wickets: {self.wickets}")

teams = {}

def create_team():
    name = input("Enter team name: ")
    teams[name] = Team(name)
    print(f"Team '{name}' created.")

def add_player_to_team():
    team_name = input("Enter team name: ")
    if team_name in teams:
        name = input("Enter player name: ")
        role = input("Enter player role (Batsman/Bowler/All-rounder): ")
        teams[team_name].add_player(Player(name, role))
        print(f"Player '{name}' added to team '{team_name}'.")
    else:
        print("Team not found.")

def view_teams():
    for team in teams.values():
        team.display_team()

def record_match():
    team1 = input("Enter Team 1: ")
    team2 = input("Enter Team 2: ")

    if team1 not in teams or team2 not in teams:
        print("One or both teams not found.")
        return

    print("Enter player performance:")
    for team in [team1, team2]:
        for player in teams[team].players:
            runs = int(input(f"Runs by {player.name}: "))
            wickets = int(input(f"Wickets by {player.name}: "))
            player.update_performance(runs, wickets)

    print("Match record updated!")

def view_player_stats():
    name = input("Enter player name: ")
    for team in teams.values():
        for player in team.players:
            if player.name == name:
                player.display_stats()
                return
    print("Player not found.")

def main():
    while True:
        print("\nCricket Management System")
        print("1. Create Team")
        print("2. Add Player to Team")
        print("3. View Teams")
        print("4. Record Match")
        print("5. View Player Stats")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            create_team()
        elif choice == "2":
            add_player_to_team()
        elif choice == "3":
            view_teams()
        elif choice == "4":
            record_match()
        elif choice == "5":
            view_player_stats()
        elif choice == "6":
            print("Exiting...!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
