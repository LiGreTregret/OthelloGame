import tkinter as tk
import tkinter.ttk as ttk

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

class GUIPlayerInputDesignForHvH:
    def __init__(self):
        # 部品
        ## root
        self.root = tk.Tk()
        self.root.title("プレイヤー設定")

        # 色リスト
        self.colors = ("白", "黒")

        ## 先攻
        self.first_frame = tk.Frame(self.root)
        self.first_label = tk.Label(self.first_frame, text="先攻", font=("游ゴシック Medium", 10))
        self.first_name_label = tk.Label(self.first_frame, text="名前", font=("游ゴシック Medium", 10))
        self.first_name_entry = tk.Entry(self.first_frame)
        self.first_color_label = tk.Label(self.first_frame, text="色", font=("游ゴシック Medium", 10))
        self.first_v = tk.StringVar()
        self.first_color_combobox = ttk.Combobox(self.first_frame, height=2, state="readonly", textvariable=self.first_v, values=self.colors, width=2)

        ## 後攻
        self.second_frame = tk.Frame(self.root)
        self.second_label = tk.Label(self.second_frame, text="後攻", font=("游ゴシック Medium", 10))
        self.second_name_label = tk.Label(self.second_frame, text="名前", font=("游ゴシック Medium", 10))
        self.second_name_entry = tk.Entry(self.second_frame)
        self.second_color_label = tk.Label(self.second_frame, text="色", font=("游ゴシック Medium", 10))
        self.second_v = tk.StringVar()
        self.second_color_combobox = ttk.Combobox(self.second_frame, height=2, state="readonly", textvariable=self.second_v, values=self.colors, width=2)
        
        ## スタートボタン
        self.start_button = tk.Button(self.root, text="スタート", font=("游ゴシック Medium", 10))

        # GUI作成
        self.first_frame.pack()
        self.first_label.pack(side=tk.TOP, anchor=tk.W, pady=2)
        self.first_name_label.pack(side=tk.LEFT, padx=2)
        self.first_name_entry.pack(side=tk.LEFT, padx=2)
        self.first_color_label.pack(side=tk.LEFT)
        self.first_color_combobox.pack(side=tk.LEFT)
        
        self.second_frame.pack()
        self.second_label.pack(side=tk.TOP, anchor=tk.W, pady=2)
        self.second_name_label.pack(side=tk.LEFT, padx=2)
        self.second_name_entry.pack(side=tk.LEFT, padx=2)
        self.second_color_label.pack(side=tk.LEFT)
        self.second_color_combobox.pack(side=tk.LEFT)

        self.start_button.pack(side=tk.TOP)

        # mainloop
        self.root.mainloop()