import pytest
from src.board.board import (
    Board,
    BoardOutputToTerminal,
    BoardOutputToGUI,
    BoardOutputContext
)
from tests.mocks.dummy_board import (
    DummyGUIGameDesign,
    DummyBoardOutput
)


def test_board_initial_state():
    """Boardクラスの初期化テスト"""
    board = Board()

    assert board.board[3][3] == 0
    assert board.board[3][4] == 1
    assert board.board[4][3] == 1
    assert board.board[4][4] == 0

    assert board.board[0][0] == -1

def test_board_output_to_terminal_output_stones(capsys):
    """BoardOutputToTerminalクラスの出力テスト"""
    board = Board()
    output = BoardOutputToTerminal(first_color=0, second_color=1)

    output.output_board(board)

    captured = capsys.readouterr().out
    assert "●" in captured or "○" in captured

def test_draw_stone_calls_create_oval_with_correct_args():
    """BoardOutputToGUIのdraw_stone()をテスト"""
    gui = DummyGUIGameDesign()
    output = BoardOutputToGUI(
        first_color="black",
        second_color="white",
        gui_game_design=gui
    )

    output.draw_stone(0, 0, "black")

    canvas = gui.canvases[0][0]
    assert len(canvas.calls) == 1

    name, args, kwargs = canvas.calls[0]
    assert name == "create_oval"
    assert kwargs["fill"] == "black"
    assert kwargs["tags"] == "stone"

# check from here
def test_output_board_draws_and_deletes_correctly():
    """BoardOutputToGUIクラスのoutput_board()をテスト"""
    gui = DummyGUIGameDesign()
    output = BoardOutputToGUI(
        first_color="black",
        second_color="white",
        gui_game_design=gui
    )

    board = Board()
    output.output_board(board)

    # (3,3) = 0 → first_color
    canvas_33 = gui.canvases[3][3]
    assert ("delete", "stone") in canvas_33.calls
    assert any(
        call[0] == "create_oval" and call[2]["fill"] == "black"
        for call in canvas_33.calls
    )

    # (3,4) = 1 → second_color
    canvas_34 = gui.canvases[3][4]
    assert ("delete", "stone") in canvas_34.calls
    assert any(
        call[0] == "create_oval" and call[2]["fill"] == "white"
        for call in canvas_34.calls
    )

    # 空マス (-1) は描画されない
    canvas_00 = gui.canvases[0][0]
    assert ("delete", "stone") in canvas_00.calls
    assert not any(call[0] == "create_oval" for call in canvas_00.calls)

def test_board_output_context_executes_set_method():
    """BoardOutputContextクラスのexecute_output_board()をテスト"""
    board = Board()
    context = BoardOutputContext()
    dummy_output = DummyBoardOutput()

    context.set_method(dummy_output)
    context.execute_output_board(board)

    assert dummy_output.called is True
