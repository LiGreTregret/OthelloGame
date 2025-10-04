from Player import HumanPlayerFromTerminal, RandomComputerPlayerFromTerminal

class PlayerManager:
    HUMAN_T = 0
    RCOM_T = 1

    player_dict = {
        HUMAN_T : HumanPlayerFromTerminal,
        RCOM_T : RandomComputerPlayerFromTerminal
    }

    def __init__(self):
        self.first_player = None
        self.second_player = None
    
    def register_first_player(self, color, name, key):
        self.first_player = PlayerManager.player_dict[key](color, name)

    def register_second_player(self, color, name, key):
        self.second_player = PlayerManager.player_dict[key](color, name)
    
    def switch(self):
        if(self.first_player != None and self.second_player != None):
            self.first_player, self.second_player = self.second_player, self.first_player