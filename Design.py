import tkinter as tk

class GUIGameDesign:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("オセロゲーム")
        self.frame_message = tk.Frame(self.root)
        self.frame_message.pack(side="top")
        self.label = tk.Label(self.frame_message, text="", font=("Arial", 10))
        self.label.pack(pady=5)
        self.frame_board = tk.Frame(self.root)
        self.frame_board.pack(side="bottom")
        self.canvases = [[None]*8 for _ in range(8)]
        self.cell_size = 50
        self._create_board_ui()
    
    def _create_board_ui(self):
        for x in range(8):
            for y in range(8):
                c = tk.Canvas(
                        self.frame_board, width=self.cell_size, height=self.cell_size, 
                        bg="green", highlightthickness=1, highlightbackground="black"
                    )
                c.grid(row=x, column=y)
                self.canvases[x][y] = c
