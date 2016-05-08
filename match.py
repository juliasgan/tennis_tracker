from team import Team
import random
class Match(object):

    def __init__(self, sets, teamA, teamB):
        self.sets = sets
        self.teamA = teamA
        self.teamB = teamB

    def winner(self):
        #Going through each of the sets and finding out who won, and then incrementing the sets to either teamA_wins or teamB_wins, and then handling
        #the tie-scenario and normal win-scenario
        teamA_wins = 0
        teamB_wins = 0

        teamA = self.teamA
        teamB = self.teamB

        for set in self.sets:
            if set.winner().name == teamA.name:
                teamA_wins += 1
            if set.winner().name == teamB.name:
                teamB_wins += 1
        if teamA_wins >= 10:  # they automatically win the match
            return teamA
        if teamB_wins >= 10:  # they automatically win the match
            return teamB
        if teamA_wins == 9 and teamB_wins == 9: #this is when the two teams are tied
            #tally games
            teamA_game_wins = 0
            teamB_game_wins = 0
            for set in self.sets:
                for game in self.games:
                    if game.winner.name == teamA.name:
                        teamA_game_wins += 1
                    if game.winner.name == teamB.name:
                        teamB_game_wins += 1
            if teamA_game_wins > teamB_game_wins: #if match score is tied, compare the # of games in all the combined sets
                return teamA #teamA has the most games when added up
            if teamB_game_wins > teamA_game_wins: #if match score is tied, compare the # of games in all the combined sets
                return teamB #teamB has the most games when added up
            if teamA_game_wins == teamB_game_wins:
                return random.choice([teamA, teamB]) #this is coin flip (heads or tails) if the game_wins is is tied



        return None










