class Game(object):
    '''game represents the tennis game with two teams and a winner'''
    '''game also represents the individual games(made up of at least 4 points) that add up to a set'''


    '''0, 15, 30, 40, Deuce, Advantage-In, Advantage-Out, Winner_of_game'''
    def __init__(self, teamA, teamB, teamA_score, teamB_score):
        self.teamA = teamA
        self.teamB = teamB
        self.teamA_score = teamA_score
        self.teamB_score = teamB_score


    def winner(self):
        difference = abs(self.teamA_score - self.teamB_score)
        if self.teamA_score >= 4: #40-0, 40-15, 40-30, deuce, Ad-in, Ad-out 4, 5, or 6 points
            if self.teamA_score - self.teamB_score >= 2: #difference must be at least 2
                return self.teamA
        if self.teamB_score >= 4: #40-0, 40-15, 40-30, deuce, Ad-in, Ad-out 4, 5, or 6 points
            if self.teamB_score - self.teamA_score >= 2: #difference must be at least 2
                return self.teamB

        return None













