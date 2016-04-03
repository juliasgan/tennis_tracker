import unittest
from match import Match
from game import Game
from set import Set
from team import Team


class MatchTestCase(unittest.TestCase):
    def test_Match(self):
        sets = []
        match = Match(sets, "Cate", 'Opponent')
        self.assertEqual(sets, [])
        self.assertEqual("Cate", match.teamA)
        self.assertEqual("Opponent", match.teamB)

    def test_winner(self):
        game1 = Game(Team("Cate"), Team("Opponent1"), Team("Cate"))
        game2 = Game(Team("Cate"), Team("Opponent1"), Team("Cate"))
        games = []
        for x in range(0, 6):
            games.append(game1)
        set1 = Set(games)
        sets = []
        for x in range(0, 18):
            sets.append(set1)

        match1 = Match(sets, game1.teamA, game1.teamB)
        self.assertEqual(game1.teamA, match1.winner())


