from PlayerManager import PlayerManager as PM
from Player import HumanPlayerFromTerminal, HumanPlayerFromGUI, RandomComputerPlayer, MostComputerPlayer
from GameMode import GameModeContext, TerminalMode, GUIMode
from Board import BoardOutputToTerminal, BoardOutputToGUI
from InputController import InputControllerGUI
from MessageOutput import MessageOutputToTerminal, MessageOutputToGUI
import tkinter as tk

class TestGameMode:
    def t_game(self):
        player_manager= PM()
        game_mode_context = GameModeContext()
        
        message_output = MessageOutputToTerminal()
        board_output = BoardOutputToTerminal()

        first_player = HumanPlayerFromTerminal(0, "White")
        second_player = RandomComputerPlayer(1, "Black", message_output)
        player_manager.register_first_player(first_player)
        player_manager.register_second_player(second_player)

        game_mode_context.set_mode(TerminalMode())
        game_mode_context.execute_game(player_manager, message_output, board_output)

    def g_game(self):
        player_manager= PM()
        game_mode_context = GameModeContext()

        root = tk.Tk()
        root.title("GameModeのテスト")
        frame_message = tk.Frame(root)
        frame_message.pack(side="top")
        frame_board = tk.Frame(root)
        frame_board.pack(side="bottom")

        board_output = BoardOutputToGUI(frame_board)
        input_controller = InputControllerGUI(board_output.canvases)
        
        message_output = MessageOutputToGUI(frame_message)

        first_player = HumanPlayerFromGUI(0, "White", input_controller, frame_message, frame_board, message_output)
        second_player = MostComputerPlayer(1, "Black", message_output)
        player_manager.register_first_player(first_player)
        player_manager.register_second_player(second_player)

        game_mode_context.set_mode(GUIMode())
        root.after(100, lambda: game_mode_context.execute_game(player_manager, message_output, board_output))
        root.mainloop()


if __name__ == "__main__":
    test_game_mode = TestGameMode()
    # test_game_mode.t_game()
    test_game_mode.g_game()