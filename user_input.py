from game import Game
from team import Team
from set import Set
from match import Match
import sys


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
                scores = string3.split("-")

                game = Game(team1, team2, int(scores[0]), int(scores[1]))
                games.append(game)
                set = Set(games)
                match = Match(sets, team1, team2)
                print "games : " + str(len(games))
                print "sets : " + str(len(sets))

                if set.winner() != None:
                    sets.append(set)
                    games = []

                if match.winner() != None:
                    games = []
                    sets = None

                string1 = ""
                string2 = ""
                string3 = ""


        return match

    def take_input(self):
        text = input("Enter game information:\n")
        print text
        match = self.parse_input(text)
        print "The number of sets: " + str(len(match.sets))
        print "The winner is: " + str(match.winner().name)















