from src.design.game_design import GUIGameDesign
from tests.mocks.dummy_board import (
    DummyGUIGameDesign
)

def test_gui_game_design(self):
    gui_game_design = GUIGameDesign()
    gui_game_design.root.mainloop()

if __name__ == "__main__":
    test_gui_game_design()