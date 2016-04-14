import unittest
from team import Team
from game import Game
from match import Match
from set import Set
from user_input import UserInput


class UserInputTestCase(unittest.TestCase):
    def test_input(self):
        games = []
        sets = []
        team1 = Team("Cate")
        team2 = Team("Opponent")
        game1 = Game(team1, team2, team1)

        for x in range(0, 6):
            games.append(game1)

        for x in range(0, 10):
            sets.append(Set(games)) #adding the sets made up of games to the match
        print len(sets)
        match = Match(sets, team1, team2)
        match1 = match




        user_input = UserInput()


        input = ""
        for x in range(0, 10):
            for x in range(0, 6):
                input += "Cate Opponent true "
        input = input[:-1]

        match2 = user_input.parse_input(input)
        self.assertEqual(match1.winner().name, match2.winner().name)


