from Design import GUIGameDesign

class DesignTest:
    def test_gui_game_design(self):
        gui_game_design = GUIGameDesign()
        gui_game_design.root.mainloop()


if __name__ == "__main__":
    design_test = DesignTest()
    design_test.test_gui_game_design()