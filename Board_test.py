from Board import Board, BoardOutputToTerminal, BoardOutputContext

class BoardOutputTest:
    # 初期状態が出力されるか確認
    def test(self):
        board = Board()
        board_output_context = BoardOutputContext()
        board_output = BoardOutputToTerminal() # ここで出力方法を選択
        board_output_context.set_method(board_output)
        board_output_context.execute_output_board(board)

if __name__ == "__main__":
    board_output_to_terminal_test = BoardOutputTest()
    board_output_to_terminal_test.test()