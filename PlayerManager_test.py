from PlayerManager import PlayerManagerForTerminal as PMT

class TestPlayerManager:
    def test_register_first_player(self):
        player_manager = PMT()
        player_manager.register_first_player(0, "White", PMT.HUMAN_T)
        assert player_manager.first_player.color == 0
        assert player_manager.first_player.name == "White"
        
    def test_register_second_player(self):
        player_manager = PMT()
        player_manager.register_second_player(0, "White", PMT.HUMAN_T)
        assert player_manager.second_player.color == 0
        assert player_manager.second_player.name == "White"