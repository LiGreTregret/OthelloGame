from GameDesign import GUIGameDesign

class GameDesignTest:
    def test_gui_game_design(self):
        gui_game_design = GUIGameDesign()
        gui_game_design.root.mainloop()

if __name__ == "__main__":
    game_design_test = GameDesignTest()
    game_design_test.test_gui_game_design()