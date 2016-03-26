class Team(object):
    """this team represents the tennis team at Cate and it contains a list of players"""

    players = []

    def __init__(self, name):
        self.name = name

    def add_player(self, player):
        self.players.append(player)
