import unittest
from player import Player


class PlayerTestCase(unittest.TestCase):
    def test_player_name(self):
        playerA = Player("Kevin")
        self.assertEqual("Kevin", playerA.name)





if __name__ == '__main__':
    unittest.main()



