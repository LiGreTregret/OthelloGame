from PlayerManager import PlayerManager as PM
from GameMode import GameModeContext, TerminalMode

class TestGameMode:
    def t_game(self):
        player_manager= PM()
        game_mode_context = GameModeContext()
        
        player_manager.register_first_player(0, "White", PM.RCOM_T)
        player_manager.register_second_player(1, "Black", PM.RCOM_T)

        game_mode_context.set_mode(TerminalMode())
        game_mode_context.execute_game(player_manager)

if __name__ == "__main__":
    test_game_mode = TestGameMode()
    test_game_mode.t_game()