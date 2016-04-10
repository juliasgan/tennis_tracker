import unittest
from team import Team
from game import Game
from match import Match
from set import Set
from user_input import UserInput


class UserInputTestCase(unittest.TestCase):
    def test_input(self):
        games = []
        game1 = Game(Team("Cate"), Team("Opponent"), Team("Cate"))
        for x in range(0, 6):
            games.append(game1)
        sets1 = [Set(games)]
        set2 = []
        user_input = UserInput()


        input = ""
        for x in range(0, 6):
            input += "Cate Opponent true "
        input = input[:-1]

        sets2 = user_input.parse_input(input)

        self.assertEqual(sets1[0].winner().name, sets2[0].winner().name)


