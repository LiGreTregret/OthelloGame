from Board import Board, BoardOutputToTerminal, BoardOutputToGUI, BoardOutputContext
import tkinter as tk

class BoardOutputTest:
    # 初期状態が出力されるか確認
    def test_to_terminal(self):
        board = Board()
        board_output_context = BoardOutputContext()
        board_output = BoardOutputToTerminal() # ここで出力方法を選択
        board_output_context.set_method(board_output)
        board_output_context.execute_output_board(board)
    
    def test_to_gui(self):
        root = tk.Tk()
        root.title("オセロのGUI出力テスト")
        board = Board()
        board_output_context = BoardOutputContext()
        board_output_context.set_method(BoardOutputToGUI(root))
        board_output_context.execute_output_board(board)
        root.mainloop()

if __name__ == "__main__":
    board_output_test = BoardOutputTest()
    board_output_test.test_to_terminal()
    board_output_test.test_to_gui() 