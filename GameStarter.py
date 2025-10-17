from Design import GUIGameDesign
from PlayerManager import PlayerManager
from Player import RandomComputerPlayer, MostComputerPlayer, LeastComputerPlayer, HumanPlayerFromGUI
from Board import Board, BoardOutputContext, BoardOutputToGUI
from InputController import InputControllerGUI
from Processing import Processing
from MessageOutput import MessageOutputContext, MessageOutputToGUI
from ResultOutput import ResultOutputContext, ResultMessageOutput

class GameStarterComponent:
    def __init__(self):
        self.COLOR = {
                0 : "白",
                1 : "黒"
            }

        self.COM_CLASS = {
            0 : RandomComputerPlayer,
            1 : MostComputerPlayer,
            2 : LeastComputerPlayer
        }

    # GUIゲーム進行メソッド
    def progress(self, processing, board, result_output_context, now, player_manager, message_output_context_game, board_output_context, gui_game_design):
        # 終了判定
        result = processing.judge_result(board)
        if result != -1:
            result_output_context.execute_output(result)
            return
        
        # 石を置く
        if now == 0:
            now_player = player_manager.first_player
        else:
            now_player = player_manager.second_player
        color = now_player.color
        name = now_player.name
        message_output_context_game.execute_output_message(f"{name}さんの番です。石({self.COLOR[color]})を置いてください。")

        board = now_player.put(board)
        gui_game_design.frame_board.after(500, lambda: board_output_context.execute_output_board(board))

        now = (now + 1) % 2

        gui_game_design.frame_board.after(500, lambda: self.progress(processing, board, result_output_context, now, player_manager, message_output_context_game, board_output_context, gui_game_design))

class GameStarterForHvHonGUI:
    def __init__(self):
        self.P1N = "p1_name"
        self.P2N = "p2_name"
        self.P1C = "p1_color"
        self.P2C = "p2_color"


    def start(self, player_dict: dict):
        # GUI作成
        gui_game_design = GUIGameDesign()

        # インスタンス化
        player_manager = PlayerManager()

        message_output_game = MessageOutputToGUI(gui_game_design)
        message_output_context_game = MessageOutputContext()
        message_output_context_game.set_message_output(message_output_game)
        
        processing = Processing()

        board = Board()

        board_output = BoardOutputToGUI(gui_game_design)
        board_output_context = BoardOutputContext()
        board_output_context.set_method(board_output)

        input_controller = InputControllerGUI(gui_game_design)

        result_output_context = ResultOutputContext()
        result_output_context.set_method(ResultMessageOutput(player_manager, message_output_game))

        game_starter_component = GameStarterComponent()

        # 名前入力
        player1_name = player_dict[self.P1N]
        player2_name = player_dict[self.P2N]
        
        # 石選択
        player1_color = player_dict[self.P1C]
        player2_color = player_dict[self.P2C]
        
        # プレイヤー登録
        player1 = HumanPlayerFromGUI(player1_color, player1_name, input_controller, gui_game_design, message_output_game)
        player2 = HumanPlayerFromGUI(player2_color, player2_name, input_controller, gui_game_design, message_output_game)

        player_manager.register_first_player(player1)
        player_manager.register_second_player(player2)

        board_output_context.execute_output_board(board)
        message_output_context_game.execute_output_message("ゲームを開始します。")

        now = 0
        gui_game_design.frame_board.after(1500, lambda: game_starter_component.progress(processing, board, result_output_context, now, player_manager, message_output_context_game, board_output_context, gui_game_design))
        
        gui_game_design.root.mainloop()

class GameStarterForHvConGUI:
    def __init__(self):
        self.HN = "hp_name"
        self.CT = "cp_comtype"
        self.HC = "hp_color"
        self.CC = "cp_color"
        self.HO = "hp_order"

    def start(self, player_dict: dict):
        # GUI作成
        gui_game_design = GUIGameDesign()

        # インスタンス化
        player_manager = PlayerManager()

        message_output_game = MessageOutputToGUI(gui_game_design)
        message_output_context_game = MessageOutputContext()
        message_output_context_game.set_message_output(message_output_game)
        
        processing = Processing()

        board = Board()

        board_output = BoardOutputToGUI(gui_game_design)
        board_output_context = BoardOutputContext()
        board_output_context.set_method(board_output)

        input_controller = InputControllerGUI(gui_game_design)

        result_output_context = ResultOutputContext()
        result_output_context.set_method(ResultMessageOutput(player_manager, message_output_game))

        game_starter_component = GameStarterComponent()

        # 名前入力
        human_player_name = player_dict[self.HN]
        com_player_name = "COM"

        # COMタイプ選択
        com_player_comtype = player_dict[self.CT]
        
        # 石選択
        human_player_color = player_dict[self.HC]
        com_player_color = player_dict[self.CC]

        # 順番選択
        human_player_order = player_dict[self.HO]

        # プレイヤー登録
        human_player = HumanPlayerFromGUI(human_player_color, human_player_name, input_controller, gui_game_design, message_output_game)
        com_player = game_starter_component.COM_CLASS[com_player_comtype](com_player_color, com_player_name, message_output_game)
        if(human_player_order == 0):
            player_manager.register_first_player(human_player)
            player_manager.register_second_player(com_player)
        else:
            player_manager.register_first_player(com_player)
            player_manager.register_second_player(human_player)

        board_output_context.execute_output_board(board)
        message_output_context_game.execute_output_message("ゲームを開始します。")

        now = 0
        gui_game_design.frame_board.after(1500, lambda: game_starter_component.progress(processing, board, result_output_context, now, player_manager, message_output_context_game, board_output_context, gui_game_design))
        
        gui_game_design.root.mainloop()

class GameStarterForCvConGUI:
    def __init__(self):
        self.P1T = "p1_comtype"
        self.P2T = "p2_comtype"
        self.P1C = "p1_color"
        self.P2C = "p2_color"

    def play(self, player_dict: dict):
        # GUI作成
        gui_game_design = GUIGameDesign()

        # インスタンス化
        player_manager = PlayerManager()

        message_output_game = MessageOutputToGUI(gui_game_design)
        message_output_context_game = MessageOutputContext()
        message_output_context_game.set_message_output(message_output_game)
        
        processing = Processing()

        board = Board()

        board_output = BoardOutputToGUI(gui_game_design)
        board_output_context = BoardOutputContext()
        board_output_context.set_method(board_output)

        result_output_context = ResultOutputContext()
        result_output_context.set_method(ResultMessageOutput(player_manager, message_output_game))

        game_launcher_component = GameStarterComponent()

        # 名前入力
        player1_name = "COM1"
        player2_name = "COM2"

        # COMタイプ選択
        player1_comtype = player_dict[self.P1T]
        player2_comtype = player_dict[self.P2T]
        
        # 石選択
        player1_color = player_dict[self.P1C]
        player2_color = player_dict[self.P2C]

        # プレイヤー登録
        player1 = game_launcher_component.COM_CLASS[player1_comtype](player1_color, player1_name, message_output_game)
        player2 = game_launcher_component.COM_CLASS[player2_comtype](player2_color, player2_name, message_output_game)
        player_manager.register_first_player(player1)
        player_manager.register_second_player(player2)

        board_output_context.execute_output_board(board)
        message_output_context_game.execute_output_message("ゲームを開始します。")

        now = 0
        gui_game_design.frame_board.after(1500, lambda: game_launcher_component.progress(processing, board, result_output_context, now, player_manager, message_output_context_game,  board_output_context, gui_game_design))
        
        gui_game_design.root.mainloop()