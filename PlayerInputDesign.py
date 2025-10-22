from GameStarter import GameStarterComponent, GameStarterForHvHonGUI, GameStarterForHvConGUI, GameStarterForCvConGUI
import tkinter as tk
import tkinter.ttk as ttk

class GUIPlayerInputDesignForHvH:
    def __init__(self):
        game_starter_component = GameStarterComponent()

        # 部品
        ## root
        self.root = tk.Tk()
        self.root.title("プレイヤー設定")

        # 色リスト
        self.colors = tuple(v[0] for v in game_starter_component.COLOR.values())
        self.color_dict = {v[0] : k for k, v in game_starter_component.COLOR.items()}
        
        ## 先攻
        self.first_frame = tk.Frame(self.root)
        self.first_label = tk.Label(self.first_frame, text="先攻", font=("游ゴシック Medium", 10))
        self.first_name_label = tk.Label(self.first_frame, text="名前", font=("游ゴシック Medium", 10))
        self.first_name_entry = tk.Entry(self.first_frame)
        self.first_color_label = tk.Label(self.first_frame, text="色", font=("游ゴシック Medium", 10))
        self.first_v = tk.StringVar()
        self.first_color_combobox = ttk.Combobox(self.first_frame, state="readonly", textvariable=self.first_v, values=self.colors, width=5)

        ## 後攻
        self.second_frame = tk.Frame(self.root)
        self.second_label = tk.Label(self.second_frame, text="後攻", font=("游ゴシック Medium", 10))
        self.second_name_label = tk.Label(self.second_frame, text="名前", font=("游ゴシック Medium", 10))
        self.second_name_entry = tk.Entry(self.second_frame)
        self.second_color_label = tk.Label(self.second_frame, text="色", font=("游ゴシック Medium", 10))
        self.second_v = tk.StringVar()
        self.second_color_combobox = ttk.Combobox(self.second_frame, height=len(self.colors), state="readonly", textvariable=self.second_v, values=self.colors, width=5)
        
        ## スタートボタン
        self.start_button = tk.Button(self.root, text="スタート", font=("游ゴシック Medium", 10), command=self.set)

        ## エラーメッセージ
        self.error_shown = False
        self.error_frame = tk.Frame(self.root)
        self.error_label = tk.Label(self.error_frame, text="異なる色を指定してください", font=("游ゴシック Medium", 10), fg="red")

        # GUI作成
        self.first_frame.pack()
        self.first_label.pack(side=tk.TOP, anchor=tk.W, pady=2)
        self.first_name_label.pack(side=tk.LEFT, padx=2)
        self.first_name_entry.pack(side=tk.LEFT, padx=2)
        self.first_color_label.pack(side=tk.LEFT)
        self.first_color_combobox.pack(side=tk.LEFT)
        self.first_color_combobox.set(self.colors[0])
        
        self.second_frame.pack()
        self.second_label.pack(side=tk.TOP, anchor=tk.W, pady=2)
        self.second_name_label.pack(side=tk.LEFT, padx=2)
        self.second_name_entry.pack(side=tk.LEFT, padx=2)
        self.second_color_label.pack(side=tk.LEFT)
        self.second_color_combobox.pack(side=tk.LEFT)
        self.second_color_combobox.set(self.colors[1])

        self.start_button.pack(side=tk.TOP)

        # mainloop
        self.root.mainloop()

    def set(self):
        game_starter_hvh = GameStarterForHvHonGUI()

        first_name = self.first_name_entry.get()
        first_color = self.color_dict[self.first_color_combobox.get()]
        second_name = self.second_name_entry.get()
        second_color = self.color_dict[self.second_color_combobox.get()]

        player_dict = {
            game_starter_hvh.P1N : first_name,
            game_starter_hvh.P1C : first_color,
            game_starter_hvh.P2N : second_name,
            game_starter_hvh.P2C : second_color
        }

        if(first_color == second_color):
            if(not(self.error_shown)):
                self.error_shown = True
                self.error_frame.pack()
                self.error_label.pack()
            return
        
        self.root.destroy()
        game_starter_hvh.start(player_dict)

class GUIPlayerInputDesignForHvC:
    def __init__(self):
        game_starter_component = GameStarterComponent()

        # 部品
        ## root
        self.root = tk.Tk()
        self.root.title("プレイヤー設定")

        # 色リスト
        self.colors = tuple(v[0] for v in game_starter_component.COLOR.values())
        self.color_dict = {v[0] : k for k, v in game_starter_component.COLOR.items()}

        # COMタイプリスト
        self.types = tuple(v[1] for v in game_starter_component.COM_TYPE.values())
        self.type_dict = {v[1] : k for k, v in game_starter_component.COM_TYPE.items()}

        ## Human
        self.human_frame = tk.Frame(self.root)
        self.human_label = tk.Label(self.human_frame, text="あなた", font=("游ゴシック Medium", 10))
        self.human_name_label = tk.Label(self.human_frame, text="名前", font=("游ゴシック Medium", 10))
        self.human_name_entry = tk.Entry(self.human_frame)
        self.human_color_label = tk.Label(self.human_frame, text="色", font=("游ゴシック Medium", 10))
        self.human_v = tk.StringVar()
        self.human_color_combobox = ttk.Combobox(self.human_frame, state="readonly", textvariable=self.human_v, values=self.colors, width=5)

        ## COM
        self.com_frame = tk.Frame(self.root)
        self.com_label = tk.Label(self.com_frame, text="COM", font=("游ゴシック Medium", 10))
        self.com_type_label = tk.Label(self.com_frame, text="タイプ", font=("游ゴシック Medium", 10))
        self.com_type_v = tk.StringVar()
        self.com_type_combobox = ttk.Combobox(self.com_frame, height=len(self.types), state="readonly", textvariable=self.com_type_v, values=self.types)
        self.com_color_label = tk.Label(self.com_frame, text="色", font=("游ゴシック Medium", 10))
        self.com_color_v = tk.StringVar()
        self.com_color_combobox = ttk.Combobox(self.com_frame, height=len(self.colors), state="readonly", textvariable=self.com_color_v, values=self.colors, width=5)
        
        ## 順番
        self.human_order_frame = tk.Frame(self.root)
        self.human_order_label = tk.Label(self.human_order_frame, text="あなたの順番", font=("游ゴシック Medium", 10))
        self.selected = tk.IntVar()
        self.first_radiobutton = tk.Radiobutton(self.human_order_frame, text="先攻", variable=self.selected, value=0)
        self.second_radiobutton = tk.Radiobutton(self.human_order_frame, text="後攻", variable=self.selected, value=1)

        ## スタートボタン
        self.start_button = tk.Button(self.root, text="スタート", font=("游ゴシック Medium", 10), command=self.set)
        
        ## エラーメッセージ
        self.error_shown = False
        self.error_frame = tk.Frame(self.root)
        self.error_label = tk.Label(self.error_frame, text="異なる色を指定してください", font=("游ゴシック Medium", 10), fg="red")

        # GUI作成
        self.human_frame.pack(anchor=tk.W)
        self.human_label.pack(side=tk.TOP, anchor=tk.W, pady=2)
        self.human_name_label.pack(side=tk.LEFT, padx=2)
        self.human_name_entry.pack(side=tk.LEFT, padx=2)
        self.human_color_label.pack(side=tk.LEFT)
        self.human_color_combobox.pack(side=tk.LEFT)
        self.human_color_combobox.set(self.colors[0])
        
        self.com_frame.pack(anchor=tk.W)
        self.com_label.pack(side=tk.TOP, anchor=tk.W, pady=2)
        self.com_type_label.pack(side=tk.LEFT, padx=2)
        self.com_type_combobox.pack(side=tk.LEFT, padx=2)
        self.com_type_combobox.set(self.types[0])
        self.com_color_label.pack(side=tk.LEFT)
        self.com_color_combobox.pack(side=tk.LEFT)
        self.com_color_combobox.set(self.colors[1])

        self.human_order_frame.pack(anchor=tk.W)
        self.human_order_label.pack(side=tk.TOP, anchor=tk.W, pady=2)
        self.first_radiobutton.pack(side=tk.LEFT, padx=2)
        self.second_radiobutton.pack(side=tk.LEFT)

        self.start_button.pack(side=tk.TOP)

        # mainloop
        self.root.mainloop()

    def set(self):
        game_starter_hvc = GameStarterForHvConGUI()

        human_name = self.human_name_entry.get()
        human_color = self.color_dict[self.human_color_combobox.get()]
        com_type = self.type_dict[self.com_type_combobox.get()]
        com_color = self.color_dict[self.com_color_combobox.get()]
        human_order = self.selected.get()

        player_dict = {
            game_starter_hvc.HN : human_name,
            game_starter_hvc.HC : human_color,
            game_starter_hvc.CT : com_type,
            game_starter_hvc.CC : com_color,
            game_starter_hvc.HO : human_order
        }

        if(human_color == com_color):
            if(not(self.error_shown)):
                self.error_shown = True
                self.error_frame.pack()
                self.error_label.pack()
            return
        
        self.root.destroy()
        game_starter_hvc.start(player_dict)

class GUIPlayerInputDesignForCvC:
    def __init__(self):
        game_starter_component = GameStarterComponent()

        # 部品
        ## root
        self.root = tk.Tk()
        self.root.title("プレイヤー設定")

        # 色リスト
        self.colors = tuple(v[0] for v in game_starter_component.COLOR.values())
        self.color_dict = {v[0] : k for k, v in game_starter_component.COLOR.items()}

        # COMタイプリスト
        self.types = tuple(v[1] for v in game_starter_component.COM_TYPE.values())
        self.type_dict = {v[1] : k for k, v in game_starter_component.COM_TYPE.items()}

        ## 先攻
        self.first_frame = tk.Frame(self.root)
        self.first_label = tk.Label(self.first_frame, text="COM1", font=("游ゴシック Medium", 10))
        self.first_type_label = tk.Label(self.first_frame, text="タイプ", font=("游ゴシック Medium", 10))
        self.first_type_v = tk.StringVar()
        self.first_type_combobox = ttk.Combobox(self.first_frame, height=len(self.types), state="readonly", textvariable=self.first_type_v, values=self.types)
        self.first_color_label = tk.Label(self.first_frame, text="色", font=("游ゴシック Medium", 10))
        self.first_color_v = tk.StringVar()
        self.first_color_combobox = ttk.Combobox(self.first_frame, state="readonly", textvariable=self.first_color_v, values=self.colors, width=5)

        ## 後攻
        self.second_frame = tk.Frame(self.root)
        self.second_label = tk.Label(self.second_frame, text="COM2", font=("游ゴシック Medium", 10))
        self.second_type_label = tk.Label(self.second_frame, text="タイプ", font=("游ゴシック Medium", 10))
        self.second_type_v = tk.StringVar()
        self.second_type_combobox = ttk.Combobox(self.second_frame, height=len(self.types), state="readonly", textvariable=self.second_type_v, values=self.types)
        self.second_color_label = tk.Label(self.second_frame, text="色", font=("游ゴシック Medium", 10))
        self.second_color_v = tk.StringVar()
        self.second_color_combobox = ttk.Combobox(self.second_frame, state="readonly", textvariable=self.second_color_v, values=self.colors, width=5)

        ## スタートボタン
        self.start_button = tk.Button(self.root, text="スタート", font=("游ゴシック Medium", 10), command=self.set)

        ## エラーメッセージ
        self.error_shown = False
        self.error_frame = tk.Frame(self.root)
        self.error_label = tk.Label(self.error_frame, text="異なる色を指定してください", font=("游ゴシック Medium", 10), fg="red")

        # GUI作成
        self.first_frame.pack()
        self.first_label.pack(side=tk.TOP, anchor=tk.W, pady=2)
        self.first_type_label.pack(side=tk.LEFT, padx=2)
        self.first_type_combobox.pack(side=tk.LEFT, padx=2)
        self.first_type_combobox.set(self.types[0])
        self.first_color_label.pack(side=tk.LEFT)
        self.first_color_combobox.pack(side=tk.LEFT)
        self.first_color_combobox.set(self.colors[0])

        self.second_frame.pack()
        self.second_label.pack(side=tk.TOP, anchor=tk.W, pady=2)
        self.second_type_label.pack(side=tk.LEFT, padx=2)
        self.second_type_combobox.pack(side=tk.LEFT, padx=2)
        self.second_type_combobox.set(self.types[0])
        self.second_color_label.pack(side=tk.LEFT)
        self.second_color_combobox.pack(side=tk.LEFT)
        self.second_color_combobox.set(self.colors[1])

        self.start_button.pack(side=tk.TOP)

        # mainloop
        self.root.mainloop()

    def set(self):
        game_starter_cvc = GameStarterForCvConGUI()

        first_type = self.type_dict[self.first_type_combobox.get()]
        first_color = self.color_dict[self.first_color_combobox.get()]
        second_type = self.type_dict[self.second_type_combobox.get()]
        second_color = self.color_dict[self.second_color_combobox.get()]

        player_dict = {
            game_starter_cvc.P1T : first_type,
            game_starter_cvc.P1C : first_color,
            game_starter_cvc.P2T : second_type,
            game_starter_cvc.P2C : second_color
        }

        if(first_color == second_color):
            if(not(self.error_shown)):
                self.error_shown = True
                self.error_frame.pack()
                self.error_label.pack()
            return
        
        self.root.destroy()
        game_starter_cvc.start(player_dict)

class GUIModeDesign:
    def __init__(self):
        # root作成
        self.root = tk.Tk()

        # 幅
        self.width = 20

        # ボタン
        self.hvh_button = tk.Button(self.root, text="2人プレイ", font=("游ゴシック Medium", 10), width=self.width, pady=5, command=self.raise_hvh)
        self.hvc_button = tk.Button(self.root, text="コンピュータと対決", font=("游ゴシック Medium", 10), width=self.width, pady=5, command=self.raise_hvc)
        self.cvc_button = tk.Button(self.root, text="コンピュータ同士の対決", font=("游ゴシック Medium", 10), width=self.width, pady=5, command=self.raise_cvc)

        # GUI作成
        self.hvh_button.pack()
        self.hvc_button.pack()
        self.cvc_button.pack()

        # mainroop
        self.root.mainloop()
    
    def raise_hvh(self):
        self.root.destroy()
        GUIPlayerInputDesignForHvH()
    
    def raise_hvc(self):
        self.root.destroy()
        GUIPlayerInputDesignForHvC()
    
    def raise_cvc(self):
        self.root.destroy()
        GUIPlayerInputDesignForCvC()