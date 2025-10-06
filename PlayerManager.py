from Player import HumanPlayerFromTerminal, RandomComputerPlayerFromTerminal, MostComputerPlayerFromTerminal, LeastComputerPlayerFromTerminal

class PlayerManager:
    HUMAN_T = 0
    RCOM_T = 1
    MCOM_T = 2
    LCOM_T = 3

    player_dict = {
        HUMAN_T : HumanPlayerFromTerminal,
        RCOM_T : RandomComputerPlayerFromTerminal,
        MCOM_T : MostComputerPlayerFromTerminal,
        LCOM_T : LeastComputerPlayerFromTerminal
    }

    def __init__(self):
        self.first_player = None
        self.second_player = None
    
    def register_first_player(self, color, name, key):
        self.first_player = PlayerManager.player_dict[key](color, name)

    def register_second_player(self, color, name, key):
        self.second_player = PlayerManager.player_dict[key](color, name)