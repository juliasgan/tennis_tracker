import unittest
from team import Team
from player import Player

class TeamTestCase(unittest.TestCase):
    def test_team_name(self):
        teamA = Team('Cate')
        self.assertEqual("Cate", teamA.name)

    def test_add_player(self):
        teamA = Team("Cate")
        playerA = Player("Kevin")
        teamA.add_player(playerA)
        self.assertEqual([playerA],teamA.players)

if __name__ == '__main__':
    unittest.main()


