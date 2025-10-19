from Player import PlayerContext, HumanPlayerFromTerminal, HumanPlayerFromGUI, RandomComputerPlayer
from MessageOutput import MessageOutputToTerminal, MessageOutputToGUI
from InputController import InputControllerGUI
from Board import Board, BoardOutputContext, BoardOutputToTerminal, BoardOutputToGUI
from GameDesign import GUIGameDesign

class TestPlayer:
    def t_put(self):
        player_context = PlayerContext()
        board = Board()
        board_output_context = BoardOutputContext()

        board_output_context.set_method(BoardOutputToTerminal())
        board_output_context.execute_output_board(board)

        instance_dict = {
            0 : HumanPlayerFromTerminal(0, "White"),
            1 : RandomComputerPlayer(0, "White", MessageOutputToTerminal())
        }

        # 置けないときのテスト用
        # board.board[3][3] = 1
        # board.board[4][4] = 1

        key = int(input("key : "))
        if(key in instance_dict.keys()):
            player_context.set_method(instance_dict[key])
            board = player_context.execute_put(board)
            board_output_context.execute_output_board(board)
        else:
            print("keyが不正です。")
        
    def g_put(self):
        gui_game_design = GUIGameDesign()

        player_context = PlayerContext()
        board = Board()
        
        board_output = BoardOutputToGUI(gui_game_design)
        board_output_context = BoardOutputContext()
        board_output_context.set_method(board_output)
        board_output_context.execute_output_board(board)

        input_controller = InputControllerGUI(gui_game_design)
        message_output = MessageOutputToGUI(gui_game_design)

        instance_dict = {
            0 : HumanPlayerFromGUI(0, "White", input_controller, gui_game_design, message_output),
            1 : RandomComputerPlayer(0, "White", MessageOutputToGUI)
        }

        # 置けないときのテスト用
        # board.board[3][3] = 1
        # board.board[4][4] = 1

        key = int(input("key : "))
        if(key in instance_dict.keys()):
            player_context.set_method(instance_dict[key])
            board = player_context.execute_put(board)
            board_output_context.execute_output_board(board)
            gui_game_design.root.mainloop()
        else:
            print("keyが不正です。")

if __name__ == '__main__':
    test_player = TestPlayer()
    # test_player.t_put()
    test_player.g_put()