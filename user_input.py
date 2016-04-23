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
        string1 = ""
        string2 = ""
        string3 = ""
        row = 1
        col = 1


        for line in inputs:
            print row
            print col

            if string1 == "":
                string1 = line
            elif string2 == "":
                string2 = line
            elif string3 == "":
                string3 = line
            if string1 != "" and string2 != "" and string3 != "":
                team1 = Team(string1)
                team2 = Team(string2)
                scores = string3.split("-")
                game = Game(team1, team2, int(scores[0]), int(scores[1]))
                games.append(game)
                set = Set(games)
                match = Match(sets, team1, team2)
                print "games : " + str(len(games))
                print "sets : " + str(len(sets))

                if set.winner() != None:
                    score = str(set.get_teamA_wins()) + '-' + str(set.get_teamB_wins())
                    self.interface.t.set(row, col, score)

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


                string3 = ""



        return match

    def take_input(self):
        text = input("Enter game information:\n")
        print text
        match = self.parse_input(text)
        print "The number of sets: " + str(len(match.sets))
        print "The winner of the overall match is: " + str(match.winner().name)
















