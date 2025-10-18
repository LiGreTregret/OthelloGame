from Design import GUIGameDesign, GUIPlayerInputDesignForHvH

class DesignTest:
    def test_gui_game_design(self):
        gui_game_design = GUIGameDesign()
        gui_game_design.root.mainloop()
    
    def test_player_input_design(self):
        GUIPlayerInputDesignForHvH()


if __name__ == "__main__":
    design_test = DesignTest()
    # design_test.test_gui_game_design()
    design_test.test_player_input_design()