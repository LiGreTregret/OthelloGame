from tests.mocks.dummy_board import (
    DummyGUIGameDesign
)

def test_gui_game_design():
    dummy_gui = DummyGUIGameDesign()
    dummy_gui.root.mainloop()
    assert dummy_gui.root.called is True