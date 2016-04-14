class Game(object):
    '''game represents the tennis game with two teams and a winner'''

    '''0, 15, 30, 40, Deuce, Advantage-In, Advantage-Out, Winner_of_game'''
    def __init__(self, teamA, teamB, teamA_score, teamB_score):
        self.teamA = teamA
        self.teamB = teamB
        self.teamA_score = teamA_score
        self.teamB_score = teamB_score


    def winner(self):
        diff = abs(self.teamA_score - self.teamB_score)
        if self.teamA_score >= 4:
            if self.teamA_score - self.teamB_score >= 2:
                return self.teamA
        if self.teamB_score >= 4:
            if self.teamB_score - self.teamA_score >= 2:
                return self.teamB

        return None













