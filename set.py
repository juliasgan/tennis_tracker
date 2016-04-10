from team import Team

class Set(object):

    #precondition: all games have the same teams
    def __init__(self, games):
        self.games = games

    def winner(self):
        teamA_wins = 0
        teamB_wins = 0

        teamA = Team("Cate")
        teamB = Team("Opponent")
        if len(self.games) > 0:
            teamA = self.games[0].teamA
            teamB = self.games[0].teamB
        print(teamA).name
        print(teamB).name
        print "Length of games: " + str(len(self.games))
        for game in self.games:
            print game.winner.name


        for game in self.games:
            print "# of games:" + str(len(self.games))
            print game.winner.name
            print teamA.name
            print teamB.name

            if game.winner.name == teamA.name:
                teamA_wins += 1
            if game.winner.name == teamB.name:
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

        print teamA_wins
        print teamB_wins
        return None







