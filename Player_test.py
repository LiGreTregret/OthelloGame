from Player import PlayerContext, HumanPlayerFromTerminal, HumanPlayerFromGUI, RandomComputerPlayer, LMComputerPlayer, Lv1ComputerPlayer
from MessageOutput import MessageOutputToTerminal, MessageOutputToGUI
from InputController import InputControllerGUI
from Board import Board, BoardOutputContext, BoardOutputToTerminal, BoardOutputToGUI
from GameDesign import GUIGameDesign

class TestPlayer:
    def t_put(self):
        player_context = PlayerContext()
        board = Board()
        board_output_context = BoardOutputContext()

        board_output_context.set_method(BoardOutputToTerminal(0, 1))
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
        
        board_output = BoardOutputToGUI("white", "black", gui_game_design)
        board_output_context = BoardOutputContext()
        board_output_context.set_method(board_output)
        board_output_context.execute_output_board(board)

        input_controller = InputControllerGUI(gui_game_design)
        message_output = MessageOutputToGUI(gui_game_design)

        instance_dict = {
            0 : HumanPlayerFromGUI(0, "White", input_controller, gui_game_design, message_output),
            1 : RandomComputerPlayer(0, "White", MessageOutputToGUI(gui_game_design)),
            2 : LMComputerPlayer(0, "white", MessageOutputToGUI(gui_game_design)),
            3 : Lv1ComputerPlayer(0, "White", MessageOutputToGUI(gui_game_design))
        }

        # 置けないときのテスト用
        board.board[3][3] = 1
        board.board[4][4] = 1

        key = int(input("key : "))
        if(key in instance_dict.keys()):
            player_context.set_method(instance_dict[key])
            board = player_context.execute_put(board)
            board_output_context.execute_output_board(board)
            gui_game_design.root.mainloop()
        else:
            print("keyが不正です。")
    
    def test_lv1_is_corner(self):
        message_output = MessageOutputToTerminal()
        lv1_com_player = Lv1ComputerPlayer(0, "White", message_output)
        
        assert lv1_com_player.is_corner(0, 0) == True
        assert lv1_com_player.is_corner(0, 1) == False
        assert lv1_com_player.is_corner(0, 7) == True
        assert lv1_com_player.is_corner(3, 7) == False
        assert lv1_com_player.is_corner(7, 7) == True

    def test_lv1_risk_to_give_corner(self):
        message_output = MessageOutputToTerminal()
        lv1_com_player = Lv1ComputerPlayer(0, "White", message_output)

        board = Board()
        board.board[0] = [-1, 1, 0, 1, 1, 1, -1, -1]

        assert lv1_com_player.risk_to_give_corner(0, 0, board) == False
        assert lv1_com_player.risk_to_give_corner(0, 6, board) == True

if __name__ == '__main__':
    test_player = TestPlayer()
    # test_player.t_put()
    test_player.g_put()