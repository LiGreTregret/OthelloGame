from PlayerManager import PlayerManagerContext, PlayerManagerForHumanVsHuman

class TestPlayerManager:
    def test_register_first_player(self):
        player_manager_context = PlayerManagerContext()
        player_manager_context.set_method(PlayerManagerForHumanVsHuman())
        player_manager_context.execute_register_first_player(0, "White")
        assert player_manager_context.player_manager.first_player.color == 0
        assert player_manager_context.player_manager.first_player.name == "White"
        
    def test_register_second_player(self):
        player_manager_context = PlayerManagerContext()
        player_manager_context.set_method(PlayerManagerForHumanVsHuman())
        player_manager_context.execute_register_second_player(1, "Black")
        assert player_manager_context.player_manager.second_player.color == 1
        assert player_manager_context.player_manager.second_player.name == "Black"