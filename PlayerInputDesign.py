from GameStarter import GameStarterForHvHonGUI
import tkinter as tk
import tkinter.ttk as ttk

class GUIPlayerInputDesignForHvH:
    def __init__(self):
        # 部品
        ## root
        self.root = tk.Tk()
        self.root.title("プレイヤー設定")

        # 色リスト
        self.colors = ("白", "黒")
        self.color_dict = {self.colors[i] : i for i in range(len(self.colors))}

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
        self.start_button = tk.Button(self.root, text="スタート", font=("游ゴシック Medium", 10), command=self.set)

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

    def set(self):
        game_starter_hvh = GameStarterForHvHonGUI()

        self.first_name = self.first_name_entry.get()
        self.first_color = self.color_dict[self.first_color_combobox.get()]
        self.second_name = self.second_name_entry.get()
        self.second_color = self.color_dict[self.second_color_combobox.get()]

        player_dict = {
            game_starter_hvh.P1N : self.first_name,
            game_starter_hvh.P1C : self.first_color,
            game_starter_hvh.P2N : self.second_name,
            game_starter_hvh.P2C : self.second_color
        }

        self.root.destroy()
        game_starter_hvh.start(player_dict)