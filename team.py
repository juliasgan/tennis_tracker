class Team(object):
    """this team represents the tennis team at Cate and it contains a list of players"""

    players = [] #creating an empty list called players

    def __init__(self, name):
        self.name = name

    def add_player(self, player):
        self.players.append(player) #adding the player to the list "players"

        #adding the possible players that could be in the class of team
        #I could also give the team a record for the season that has been played so far
