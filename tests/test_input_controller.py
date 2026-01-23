from src.design.game_design import GUIGameDesign
from src.controller.input_controller import InputControllerGUI

from unittest.mock import MagicMock

def test_on_click():
    gui_game_design = GUIGameDesign()
    input_controller = InputControllerGUI(gui_game_design)
    
    input_controller._on_click(0, 1)
    assert input_controller.clicked_pos == (0, 1)

    input_controller._on_click(7, 7)
    assert input_controller.clicked_pos == (7, 7)

def test_wait_for_click_no_gui():
    mock_root = MagicMock()

    gui_mock = MagicMock()
    gui_mock.root = mock_root

    input_controller = InputControllerGUI(gui_mock)

    test_cases = [(x, y) for x in range(8) for y in range(8)]

    for x, y in test_cases:
        def side_effect():
            input_controller.clicked_pos = (x, y)
        
        mock_root.update.side_effect = side_effect
        pos = input_controller.wait_for_click(mock_root)
        assert pos == (x, y)