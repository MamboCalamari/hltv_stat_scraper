class TestInput:

    def __init__(self):
        self.teams = []

    def enter_teams(self):
        self.teams.append(raw_input("Team1: "))
        self.teams.append(raw_input("Team2: "))

    def get_teams(self):
        return self.teams