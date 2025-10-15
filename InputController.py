from Design import GUIGameDesign

class InputControllerGUI:
    def __init__(self, gui_game_design: GUIGameDesign):
        self.canvases = gui_game_design.canvases
        self.clicked_pos = None
        for x in range(8):
            for y in range(8):
                c = self.canvases[x][y]
                c.bind("<Button-1>", lambda e, x=x, y=y: self._on_click(x, y))
        
    def _on_click(self, x, y):
        self.clicked_pos = (x, y)
    
    def wait_for_click(self, root):
        while(self.clicked_pos is None): root.update()
        pos = self.clicked_pos
        self.clicked_pos = None
        return pos