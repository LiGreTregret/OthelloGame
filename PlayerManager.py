from Player import HumanPlayerFromTerminal, \
                   HumanPlayerFromGUI, \
                   RandomComputerPlayer, \
                   MostComputerPlayer, \
                   LeastComputerPlayer

class PlayerManagerForTerminal:
    HUMAN_T = 0
    RCOM = 1
    MCOM = 2
    LCOM = 3

    player_dict = {
        HUMAN_T : HumanPlayerFromTerminal,
        RCOM : RandomComputerPlayer,
        MCOM : MostComputerPlayer,
        LCOM : LeastComputerPlayer
    }

    def __init__(self):
        self.first_player = None
        self.second_player = None
    
    def register_first_player(self, color, name, key):
        self.first_player = PlayerManagerForTerminal.player_dict[key](color, name)

    def register_second_player(self, color, name, key):
        self.second_player = PlayerManagerForTerminal.player_dict[key](color, name)