from design.putable_highlighter import PutableHighlighter
from src.othello.Board import Board, BoardOutputToGUI
import tkinter as tk

class PutableHighLighterTest:
    def test(self):
        root = tk.Tk()
        board = Board()
        board_output = BoardOutputToGUI(root)
        board_output.output_board(board)

        putable_highlighter = PutableHighlighter(board_output.frame_board)

        root.after(1000, lambda: putable_highlighter.highlight(0, board))
        root.after(2000, lambda: putable_highlighter.clear())
        root.after(3000, lambda: putable_highlighter.highlight(1, board))
        root.after(4000, lambda: putable_highlighter.clear())

        root.mainloop()

if __name__ == "__main__":
    putable_highlighter_test = PutableHighLighterTest()
    putable_highlighter_test.test()