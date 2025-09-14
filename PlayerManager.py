from abc import ABC, abstractmethod
from Player import HumanPlayerFromTerminal

class PlayerManager(ABC):
    @abstractmethod
    def __init__(self):
        self.first_player = None
        self.second_player = None
    
    def register_first_player(self, name, color):
        pass

    def register_second_player(self, name, color):
        pass

class PlayerManagerForHumanVsHumanOnTerminal(PlayerManager):
    def __init__(self):
        self.first_player = None
        self.second_player = None
    
    def register_first_player(self, color, name):
        self.first_player = HumanPlayerFromTerminal(color, name)

    def register_second_player(self, color, name):
        self.second_player = HumanPlayerFromTerminal(color, name)
    
class PlayerManagerContext:
    def __init__(self):
        self.player_manager = None

    def set_method(self, player_manager: PlayerManager):
        self.player_manager = player_manager
    
    def execute_register_first_player(self, color, name):
        if self.player_manager is not None:
            self.player_manager.register_first_player(color, name)
        else:
            print("No method set up")
    
    def execute_register_second_player(self, color, name):
        if self.player_manager is not None:
            self.player_manager.register_second_player(color, name)
        else:
            print("No method set up")