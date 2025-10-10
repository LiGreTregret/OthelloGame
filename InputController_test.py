from Board import Board, BoardOutputToGUI, BoardOutputContext
from InputController import InputControllerGUI
import tkinter as tk

class TestInputController:
    def test_on_click(self):
        root = tk.Tk()
        frame_board = tk.Frame(root)
        frame_board.pack()
        board_output = BoardOutputToGUI(frame_board)
        input_controller = InputControllerGUI(board_output.canvases)
        
        input_controller._on_click(0, 1)
        assert input_controller.clicked_pos == (0, 1)

        input_controller._on_click(7, 7)
        assert input_controller.clicked_pos == (7, 7)
    
    def t_wait_for_click(self):
        root = tk.Tk()
        frame_board = tk.Frame(root)
        frame_board.pack()

        board = Board()
        board_output = BoardOutputToGUI(frame_board)
        board_output_context = BoardOutputContext()
        board_output_context.set_method(board_output)
        board_output_context.execute_output_board(board)

        input_controller = InputControllerGUI(board_output.canvases)

        pos = input_controller.wait_for_click(root)
        print(pos)

if __name__ == "__main__":
    input_controller_test = TestInputController()
    input_controller_test.t_wait_for_click()