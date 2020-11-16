class Task:
    def __init__(self, description, team):
        self.description = description
        self.team = team

    def __add__(self, other):
        return Task(self.description + "\n" + other.description, self.team + ", " + other.team)
