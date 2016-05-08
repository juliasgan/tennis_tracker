from team import Team

class Set(object):

    #precondition: all games have the same teams
    def __init__(self, games, schoolA, schoolB, playersA, playersB):
        self.games = games
        teamA = Team(schoolA)
        teamB = Team(schoolB)

        for player in playersA.split(","): #splitting the names by the comma (in the input-Kevin:1,) and adding it to the player list
            teamA.add_player(player)

        for player in playersB.split(","): #same thing with the opponent
            teamB.add_player(player)


        self.teamA = teamA
        self.teamB = teamB
        self.playersA = playersA
        self.playersB = playersB


    def winner(self):
        teamA_wins = 0
        teamB_wins = 0

        teamA = self.teamA
        teamB = self.teamB
        if len(self.games) > 0:
            teamA = self.games[0].teamA
            teamB = self.games[0].teamB


        for game in self.games:
        #This is going through each game and checking who won the game then incrementing teamA_wins or teamB_wins
            if game.winner().name == teamA.name:
                teamA_wins += 1
            if game.winner().name == teamB.name:
                teamB_wins += 1
        if teamA_wins >= 7: #if the score is 7-6 or 7-5 for teamA (teamA wins)
            return teamA
        if teamB_wins >= 7: #if the score is 7-6 or 7-5 for teamB (teamB wins)
            return teamB
        if teamA_wins > 5: #7-5 for teamA
            if abs(teamB_wins - teamA_wins) > 2: #difference between wins and losses have to be at least 2 unless you go to a tiebreak
                return teamA
        if teamB_wins > 5: #7-5 for teamB
            if abs(teamB_wins - teamA_wins) > 2:
                return teamB


        return None

    def get_teamA_wins(self):
        teamA_wins = 0
        teamA = Team("Cate")
        teamB = Team("Opponent")
        for game in self.games:
            if game.winner().name == teamA.name:
                teamA_wins += 1
        return teamA_wins


    def get_teamB_wins(self):
        teamB_wins = 0
        teamA = Team("Cate")
        teamB = Team("Opponent")
        for game in self.games:
            if game.winner().name == teamB.name:
                teamB_wins += 1
        return teamB_wins







