from src.board.board import (
    Board,
    BoardOutput
)

class DummyCanvas:
    """Tkinter Canvasのモック"""
    def __init__(self):
        self.calls = []

    def create_oval(self, *args, **kwargs):
        self.calls.append(("create_oval", args, kwargs))

    def delete(self, tag):
        self.calls.append(("delete", tag))


class DummyGUIGameDesign:
    """GUIGameDesignのモック"""
    def __init__(self):
        self.cell_size = 100
        self.stone_margin = 10
        self.canvases = [
            [DummyCanvas() for _ in range(8)]
            for _ in range(8)
        ]


class DummyBoardOutput(BoardOutput):
    """BoardOutputContextのダミー"""
    def __init__(self):
        self.called = False

    def output_board(self, board: Board):
        self.called = True