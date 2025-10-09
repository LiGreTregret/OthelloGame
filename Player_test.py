from Player import PlayerContext, HumanPlayerFromTerminal, HumanPlayerFromGUI, RandomComputerPlayerFromTerminal
from InputController import InputControllerGUI
from Board import Board, BoardOutputContext, BoardOutputToTerminal, BoardOutputToGUI
import tkinter as tk

class TestPlayer:
    def t_put(self):
        player_context = PlayerContext()
        board = Board()
        board_output_context = BoardOutputContext()

        board_output_context.set_method(BoardOutputToTerminal())
        board_output_context.execute_output_board(board)

        instance_dict = {
            0 : HumanPlayerFromTerminal(0, "White"),
            1 : RandomComputerPlayerFromTerminal(0, "White")
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
        root = tk.Tk()
        frame_message = tk.Frame(root)
        frame_message.pack(side="top")
        frame_board = tk.Frame(root)
        frame_board.pack(side="bottom")

        player_context = PlayerContext()
        board = Board()
        
        board_output = BoardOutputToGUI(frame_board)
        board_output_context = BoardOutputContext()
        board_output_context.set_method(board_output)
        board_output_context.execute_output_board(board)

        input_controller = InputControllerGUI(board_output.canvases)

        instance_dict = {
            0 : HumanPlayerFromGUI(0, "White", input_controller, frame_message, frame_board)
        }

        # 置けないときのテスト用
        # board.board[3][3] = 1
        # board.board[4][4] = 1

        key = int(input("key : "))
        if(key in instance_dict.keys()):
            player_context.set_method(instance_dict[key])
            board = player_context.execute_put(board)
            board_output_context.execute_output_board(board)
            root.mainloop()
        else:
            print("keyが不正です。")

if __name__ == '__main__':
    test_player = TestPlayer()
    test_player.t_put()
    test_player.g_put()