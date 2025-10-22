from Board import Board, BoardOutputToTerminal, BoardOutputToGUI, BoardOutputContext
from GameDesign import GUIGameDesign

class BoardOutputTest:
    # 初期状態が出力されるか確認
    def test_to_terminal(self):
        board = Board()
        board_output_context = BoardOutputContext()
        board_output = BoardOutputToTerminal(1, 0) # ここで出力方法を選択
        board_output_context.set_method(board_output)
        board_output_context.execute_output_board(board)
    
    def test_to_gui(self):
        board = Board()
        gui_game_design = GUIGameDesign()
        board_output_context = BoardOutputContext()
        board_output_context.set_method(BoardOutputToGUI("yellow", "blue", gui_game_design))
        board_output_context.execute_output_board(board)
        gui_game_design.root.mainloop()

if __name__ == "__main__":
    board_output_test = BoardOutputTest()
    board_output_test.test_to_terminal()
    board_output_test.test_to_gui() 