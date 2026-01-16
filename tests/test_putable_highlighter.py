from src.design.putable_highlighter import PutableHighlighter
from src.design.game_design import GUIGameDesign
from src.board.board import Board, BoardOutputToGUI

class PutableHighLighterTest:
    def test(self):
        gui_game_design = GUIGameDesign()
        board = Board()
        board_output = BoardOutputToGUI("white", "black", gui_game_design)
        board_output.output_board(board)

        putable_highlighter = PutableHighlighter(gui_game_design.frame_board)

        gui_game_design.root.after(1000, lambda: putable_highlighter.highlight(0, board))
        gui_game_design.root.after(2000, lambda: putable_highlighter.clear())
        gui_game_design.root.after(3000, lambda: putable_highlighter.highlight(1, board))
        gui_game_design.root.after(4000, lambda: putable_highlighter.clear())

        gui_game_design.root.mainloop()

if __name__ == "__main__":
    putable_highlighter_test = PutableHighLighterTest()
    putable_highlighter_test.test()