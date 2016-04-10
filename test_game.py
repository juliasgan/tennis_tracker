import unittest
#http://docs.python-guide.org/en/latest/writing/tests/
from team import Team
from game import Game

class GameTestCase(unittest.TestCase):
    def test_winner(self):
        teamA = Team("Cate")
        teamB = Team("Opponent")
        game = Game(teamA,teamB,teamA)
        self.assertEqual(teamA, game.winner)


