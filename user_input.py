from game import Game
from team import Team
from set import Set
from match import Match
from interface import Interface
import sys

#Will count the number of games individually, and then add them to the sets, then add up the sets to match
#The most matches a team needs to win the whole match is just ten matches (closest score: 10-8)

class UserInput(object):
    def __init__(self):
        print ""

    def parse_input(self, input):

        self.interface = Interface()

        inputs = input.split(" ")

        games = []
        sets = []
        game = None
        teamA_name = ""
        teamB_name = ""
        playersA = ""
        playersB = ""
        game_score = ""
        row = 1
        col = 1
        num_sets = 0

        for line in inputs:

            if teamA_name == "":
                teamA_name = line
            elif teamB_name == "":
                teamB_name = line
            elif playersA == "":
                playersA = line
            elif playersB == "":
                playersB = line
            elif game_score == "":
                game_score = line


            if teamA_name != "" and teamB_name != "" and playersA != "" and playersB != "" and game_score != "":
                team1 = Team(teamA_name)
                team2 = Team(teamB_name)
                scores = game_score.split("-")
                game = Game(team1, team2, int(scores[0]), int(scores[1]))
                games.append(game)
                print "num_sets: " + str(num_sets)
                set = Set(games, teamA_name, teamB_name, playersA.split(",")[num_sets%3], playersB.split(",")[num_sets%3])
                match = Match(sets, team1, team2)
                print "games : " + str(len(games))


                if set.winner() != None:
                    num_sets += 1
                    score = str(set.get_teamA_wins()) + '-' + str(set.get_teamB_wins())
                    self.interface.t.set(row, col, score)
                    if row == 1 and col == 1:
                        self.interface.t.set(4, col, set.playersA)
                        self.interface.t.set(row, 4, set.playersB)
                    if row == 2 and col == 2:
                        self.interface.t.set(4, col, set.playersA)
                        self.interface.t.set(row, 4, set.playersB)
                    if row == 3 and col == 3:
                        self.interface.t.set(4, 3, set.playersA)
                        self.interface.t.set(3, 4, set.playersB)
                        self.interface.t.set(4, 4, "Players")




                    print "row: " + str(row) + " col: " + str(col) + " score: " + str(score)
                    print "set.playersA: " + str(set.playersA)
                    print "set.playersB: " + str(set.playersB)

                    if col < 3:
                        col += 1
                    else:
                        col = 1
                        row += 1
                    if row == 4:
                        col = 1
                        row = 1
                    sets.append(set)
                    games = []

                if match.winner() != None:
                    games = []
                    sets = None


                game_score = ""
                
        return match

    def take_input(self):
        text = input("Enter game information:\n")
        print text
        match = self.parse_input(text)
        print "The number of sets: " + str(len(match.sets))
        print "The winner of the overall match is: " + str(match.winner().name)
















