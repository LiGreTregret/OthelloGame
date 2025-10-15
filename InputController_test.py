from Design import GUIGameDesign
from Board import Board, BoardOutputToGUI, BoardOutputContext
from InputController import InputControllerGUI

class TestInputController:
    def test_on_click(self):
        gui_game_design = GUIGameDesign()
        input_controller = InputControllerGUI(gui_game_design)
        
        input_controller._on_click(0, 1)
        assert input_controller.clicked_pos == (0, 1)

        input_controller._on_click(7, 7)
        assert input_controller.clicked_pos == (7, 7)
    
    def t_wait_for_click(self):
        gui_game_design = GUIGameDesign()

        board = Board()
        board_output = BoardOutputToGUI(gui_game_design)
        board_output_context = BoardOutputContext()
        board_output_context.set_method(board_output)
        board_output_context.execute_output_board(board)

        input_controller = InputControllerGUI(gui_game_design)

        pos = input_controller.wait_for_click(gui_game_design.root)
        print(pos)

if __name__ == "__main__":
    input_controller_test = TestInputController()
    input_controller_test.t_wait_for_click()