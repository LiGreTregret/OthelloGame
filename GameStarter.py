from GameDesign import GUIGameDesign
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
                0 : ["白", "white"],
                1 : ["黒", "black"]
            }

        self.COM_TYPE = {
            0 : [RandomComputerPlayer, "ランダム"],
            1 : [MostComputerPlayer, "最多選択"],
            2 : [LeastComputerPlayer, "最少選択"]
        }

    # GUIゲーム進行メソッド
    def progress(self, processing, board, result_output_context, now, player_manager, first_color, second_color, message_output_context_game, board_output_context, gui_game_design):
        # 終了判定
        result = processing.judge_result(board)
        if result != -1:
            result_output_context.execute_output(result)
            return
        
        # 石を置く
        if(now == 0):
            now_player = player_manager.first_player
            color = first_color
        else:
            now_player = player_manager.second_player
            color = second_color
        name = now_player.name
        message_output_context_game.execute_output_message(f"{name}さんの番です。石({color})を置いてください。")

        board = now_player.put(board)
        gui_game_design.frame_board.after(500, lambda: board_output_context.execute_output_board(board))

        now = (now + 1) % 2

        gui_game_design.frame_board.after(500, lambda: self.progress(processing, board, result_output_context, now, player_manager, first_color, second_color, message_output_context_game, board_output_context, gui_game_design))

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

        input_controller = InputControllerGUI(gui_game_design)

        result_output_context = ResultOutputContext()
        result_output_context.set_method(ResultMessageOutput(player_manager, message_output_game))

        game_starter_component = GameStarterComponent()

        # 名前入力
        player1_name = player_dict[self.P1N]
        player2_name = player_dict[self.P2N]
        
        # プレイヤー登録
        player1 = HumanPlayerFromGUI(0, player1_name, input_controller, gui_game_design, message_output_game)
        player2 = HumanPlayerFromGUI(1, player2_name, input_controller, gui_game_design, message_output_game)

        player_manager.register_first_player(player1)
        player_manager.register_second_player(player2)

        # 石選択
        player1_color = player_dict[self.P1C]
        player2_color = player_dict[self.P2C]

        first_color_jp = game_starter_component.COLOR[player1_color][0]
        second_color_jp = game_starter_component.COLOR[player2_color][0]
        first_color_en = game_starter_component.COLOR[player1_color][1]
        second_color_en = game_starter_component.COLOR[player2_color][1]

        board_output = BoardOutputToGUI(first_color_en, second_color_en, gui_game_design)
        board_output_context = BoardOutputContext()
        board_output_context.set_method(board_output)

        board_output_context.execute_output_board(board)
        message_output_context_game.execute_output_message("ゲームを開始します。")

        now = 0
        gui_game_design.frame_board.after(1500, lambda: game_starter_component.progress(processing, board, result_output_context, now, player_manager, first_color_jp, second_color_jp, message_output_context_game, board_output_context, gui_game_design))
        
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

        input_controller = InputControllerGUI(gui_game_design)

        result_output_context = ResultOutputContext()
        result_output_context.set_method(ResultMessageOutput(player_manager, message_output_game))

        game_starter_component = GameStarterComponent()

        # 名前入力
        human_player_name = player_dict[self.HN]
        com_player_name = "COM"

        # COMタイプ選択
        com_player_comtype = player_dict[self.CT]
        
        # 順番選択
        human_player_order = player_dict[self.HO]
        com_player_order = (human_player_order + 1) % 2

        # 石選択
        human_player_color = player_dict[self.HC]
        com_player_color = player_dict[self.CC]

        # プレイヤー登録
        human_player = HumanPlayerFromGUI(human_player_order, human_player_name, input_controller, gui_game_design, message_output_game)
        com_player = game_starter_component.COM_TYPE[com_player_comtype][0](com_player_order, com_player_name, message_output_game)
        if(human_player_order == 0):
            player_manager.register_first_player(human_player)
            player_manager.register_second_player(com_player)
            first_color = human_player_color
            second_color = com_player_color
        else:
            player_manager.register_first_player(com_player)
            player_manager.register_second_player(human_player)
            first_color = com_player_color
            second_color = human_player_color

        first_color_jp = game_starter_component.COLOR[first_color][0]
        second_color_jp = game_starter_component.COLOR[second_color][0]
        first_color_en = game_starter_component.COLOR[first_color][1]
        second_color_en = game_starter_component.COLOR[second_color][1]

        board_output = BoardOutputToGUI(first_color_en, second_color_en, gui_game_design)
        board_output_context = BoardOutputContext()
        board_output_context.set_method(board_output)

        board_output_context.execute_output_board(board)
        message_output_context_game.execute_output_message("ゲームを開始します。")

        now = 0
        gui_game_design.frame_board.after(1500, lambda: game_starter_component.progress(processing, board, result_output_context, now, player_manager, first_color_jp, second_color_jp, message_output_context_game, board_output_context, gui_game_design))
        
        gui_game_design.root.mainloop()

class GameStarterForCvConGUI:
    def __init__(self):
        self.P1T = "p1_comtype"
        self.P2T = "p2_comtype"
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

        result_output_context = ResultOutputContext()
        result_output_context.set_method(ResultMessageOutput(player_manager, message_output_game))

        game_starter_component = GameStarterComponent()

        # 名前入力
        player1_name = "COM1"
        player2_name = "COM2"

        # COMタイプ選択
        player1_comtype = player_dict[self.P1T]
        player2_comtype = player_dict[self.P2T]

        # プレイヤー登録
        player1 = game_starter_component.COM_TYPE[player1_comtype][0](0, player1_name, message_output_game)
        player2 = game_starter_component.COM_TYPE[player2_comtype][0](1, player2_name, message_output_game)
        player_manager.register_first_player(player1)
        player_manager.register_second_player(player2)

        # 石選択
        player1_color = player_dict[self.P1C]
        player2_color = player_dict[self.P2C]

        first_color_jp = game_starter_component.COLOR[player1_color][0]
        second_color_jp = game_starter_component.COLOR[player2_color][0]
        first_color_en = game_starter_component.COLOR[player1_color][1]
        second_color_en = game_starter_component.COLOR[player2_color][1]

        board_output = BoardOutputToGUI(first_color_en, second_color_en, gui_game_design)
        board_output_context = BoardOutputContext()
        board_output_context.set_method(board_output)

        board_output_context.execute_output_board(board)
        message_output_context_game.execute_output_message("ゲームを開始します。")

        now = 0
        gui_game_design.frame_board.after(1500, lambda: game_starter_component.progress(processing, board, result_output_context, now, player_manager, first_color_jp, second_color_jp, message_output_context_game, board_output_context, gui_game_design))
        
        gui_game_design.root.mainloop()