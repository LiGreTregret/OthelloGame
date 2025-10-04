from PlayerManager import PlayerManager as PM

class TestPlayerManager:
    def test_register_first_player(self):
        player_manager = PM()
        player_manager.register_first_player(0, "White", PM.HUMAN_T)
        assert player_manager.first_player.color == 0
        assert player_manager.first_player.name == "White"
        
    def test_register_second_player(self):
        player_manager = PM()
        player_manager.register_second_player(0, "White", PM.HUMAN_T)
        assert player_manager.second_player.color == 0
        assert player_manager.second_player.name == "White"
    
    def test_switch(self):
        player_manager = PM()
        player_manager.register_first_player(0, "White", PM.HUMAN_T)
        player_manager.register_second_player(1, "Black", PM.HUMAN_T)
        assert player_manager.first_player.color == 0
        assert player_manager.first_player.name == "White"
        assert player_manager.second_player.color == 1
        assert player_manager.second_player.name == "Black"