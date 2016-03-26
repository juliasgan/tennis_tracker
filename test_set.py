import unittest
from game import Game
from set import Set
from team import Team

class SetTestCase(unittest.TestCase):
    def test_games(self):
        game1 = Game(Team("Cate"), Team("Opponent1"), Team("Cate"))
        game2 = Game(Team("Cate"), Team("Opponent2"), Team("Cate"))
        set = Set([game1,game2])
        self.assertEqual([game1,game2],set.games)

    def test_winner(self):
        game1 = Game(Team("Cate"), Team("Opponent1"), Team("Cate"))
        game2 = Game(Team("Cate"), Team("Opponent2"), Team("Cate"))
        set1 = Set([game1, game2])
        self.assertEqual(None, set1.winner())

        games = []
        for x in range(0,6):
            games.append([game1])
        set2 = Set(games)
        self.assertEqual(game1.teamA, set2.winner())









