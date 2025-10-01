from PlayerManager import PlayerManagerContext, PlayerManagerForHumanVsHuman
from GameMode import GameModeContext, TerminalMode

class TestGameMode:
    def t_game(self):
        player_manager_context = PlayerManagerContext()
        game_mode_context = GameModeContext()
        
        player_manager_context.set_method(PlayerManagerForHumanVsHuman())
        player_manager_context.execute_register_first_player(0, "White")
        player_manager_context.execute_register_second_player(1, "Black")

        game_mode_context.set_mode(TerminalMode())
        game_mode_context.execute_game(player_manager_context.player_manager)

if __name__ == "__main__":
    test_game_mode = TestGameMode()
    test_game_mode.t_game()