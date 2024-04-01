class Game():

    def __init__(self, id, team1, team2):
        self.id = id
        self.team1 = team1
        self.team2 = team2
        self.team1_factor = self.__set_factor(self.team1, self.team2)
        self.team2_factor = self.__set_factor(self.team2, self.team1)
        return

    def get_teams(self):
        return [[self.team1, self.team1_factor], [self.team2, self.team2_factor]]

    def __set_factor(self, team1, team2):
        return team1.get_factor() - team2.get_factor()
