from player import Player

class PlayerManager:
    def __init__(self):
        self.first_player = None
        self.second_player = None
    
    def register_first_player(self, player: Player):
        self.first_player = player
    
    def register_second_player(self, player: Player):
        self.second_player = player