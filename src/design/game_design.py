import tkinter as tk

class GUIGameDesign:
    def __init__(self):
        # root作成
        self.root = tk.Tk()
        self.root.title("オセロゲーム")

        # メッセージ作成
        self.frame_message = tk.Frame(self.root)
        self.frame_message.pack(side="top")
        self.label = tk.Label(self.frame_message, text="", font=("游ゴシック Medium", 10))
        self.label.pack(pady=5)

        # 盤面作成
        self.frame_board = tk.Frame(self.root)
        self.frame_board.pack(side="bottom", fill="both", expand=True)
        self.frame_board.bind("<Configure>", self._on_frame_board_configure)

        self.canvases = [[None]*8 for _ in range(8)]

        self._cell_size: float = 50.0
        self._stone_margin: float = 5.0

        self._create_board_ui()

    @property
    def cell_size(self) -> float:
        return self._cell_size

    @property
    def stone_margin(self) -> float:
        return self._stone_margin

    def _on_frame_board_configure(self, event):
        """「frame_boardの<Configure>」イベントでキャンバスをスケーリングする。"""

        if event.widget is not self.frame_board:
            return

        prev_cell_size = self._cell_size
        self._cell_size = min(event.width, event.height) / 8
        scale_ratio = self._cell_size / prev_cell_size
        self._stone_margin *= scale_ratio

        for row in self.canvases:
            for cell_canvas in row:
                cell_canvas.config(width=self._cell_size, height=self._cell_size)
                cell_canvas.scale("stone", 0, 0, scale_ratio, scale_ratio)
    
    def _create_board_ui(self):
        for x in range(8):
            for y in range(8):
                c = tk.Canvas(
                        self.frame_board, width=self.cell_size, height=self.cell_size, 
                        bg="green", highlightthickness=1, highlightbackground="black"
                    )
                c.grid(row=x, column=y)
                self.canvases[x][y] = c