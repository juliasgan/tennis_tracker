from team import Team
import random
class Match(object):

    def __init__(self, sets, teamA, teamB):
        self.sets = sets
        self.teamA = teamA
        self.teamB = teamB

    def winner(self):
        teamA_wins = 0
        teamB_wins = 0

        teamA = self.teamA
        teamB = self.teamB

        for set in self.sets:
            if set.winner().name == teamA.name:
                teamA_wins += 1
            if set.winner().name == teamB.name:
                teamB_wins += 1
        if teamA_wins >= 10:  # they win the match
            return teamA
        if teamB_wins >= 10:  # they win the match
            return teamB
        if teamA_wins == 9 and teamB_wins == 9:
            #tally games
            teamA_game_wins = 0
            teamB_game_wins = 0
            for set in self.sets:
                for game in self.games:
                    if game.winner.name == teamA.name:
                        teamA_game_wins += 1
                    if game.winner.name == teamB.name:
                        teamB_game_wins += 1
            if teamA_game_wins > teamB_game_wins:
                return teamA
            if teamB_game_wins > teamA_game_wins:
                return teamB
            if teamA_game_wins == teamB_game_wins:
                return random.choice([teamA, teamB])




        print teamA_wins
        print teamB_wins
        return None










