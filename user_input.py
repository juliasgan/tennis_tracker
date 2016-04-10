from game import Game
from team import Team
from set import Set


class UserInput(object):
    def __init__(self):
        print ""

    def parse_input(self, input):

        inputs = input.split(" ")

        games = []
        sets = []
        game = None
        string1 = ""
        string2 = ""
        string3 = ""

        for line in inputs:

            if string1 == "":
                string1 = line
            elif string2 == "":
                string2 = line
            elif string3 == "":
                string3 = line
            if string1 != "" and string2 != "" and string3 != "":
                team1 = Team(string1)
                team2 = Team(string2)
                team3 = None
                if string3 == "true":
                    team3 = team1
                else:
                    team3 = team2

                game = Game(team1, team2, team3)
                games.append(game)
                set = Set(games)
                print len(games)

                if set.winner() != None:
                    sets.append(set)
                    games = []
                    set = None
                string1 = ""
                string2 = ""
                string3 = ""


        return sets





