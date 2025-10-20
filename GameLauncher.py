from abc import ABC, abstractmethod
from PlayerInputDesign import GUIModeDesign
from PlayerManager import PlayerManager
from Player import HumanPlayerFromTerminal, RandomComputerPlayer, MostComputerPlayer, LeastComputerPlayer
from Board import Board, BoardOutputContext, BoardOutputToTerminal
from Processing import Processing
from MessageOutput import MessageOutputContext, MessageOutputToTerminal
from ResultOutput import ResultOutputContext, ResultMessageOutput
from time import sleep

class GameLauncherComponent:
    def __init__(self):
        self.COLOR = {
                0 : "白",
                1 : "黒"
            }
        
        self.COM_INDEX = (
                "0 : ランダム\n"
                "1 : 1番多くひっくり返せる場所に置く\n"
                "2 : 1番少なくひっくり返せる場所に置く"
            )

        self.COM_CLASS = {
            0 : RandomComputerPlayer,
            1 : MostComputerPlayer,
            2 : LeastComputerPlayer
        }

class GameLauncher(ABC):
    @abstractmethod
    def play(self):
        pass

class GameLauncherForHvHonTerminal(GameLauncher):
    def play(self):
        # インスタンス化など前準備
        player_manager = PlayerManager()

        message_output = MessageOutputToTerminal()
        message_output_context = MessageOutputContext()
        message_output_context.set_message_output(message_output)

        processing = Processing()
        
        board = Board()
        board_output_context = BoardOutputContext()
        board_output_context.set_method(BoardOutputToTerminal())

        result_output_context = ResultOutputContext()
        result_output_context.set_method(ResultMessageOutput(player_manager, message_output))

        game_launcher_component = GameLauncherComponent()

        # 名前入力
        message_output_context.execute_output_message("1人目の名前を入力してください。")
        player1_name = str(input("> "))
        message_output_context.execute_output_message("2人目の名前を入力してください。")
        player2_name = str(input("> "))
        
        # 石選択
        message_output_context.execute_output_message("白の石を使うプレイヤーの数字を選んでください。")
        message_output_context.execute_output_message(f"0:{player1_name} 1:{player2_name}")
        white = int(input("数字 > "))
        if(white == 0):
            player1_color = 0
            player2_color = 1
        else:
            player1_color = 1
            player2_color = 0
        
        # 先攻選択
        message_output_context.execute_output_message("先攻のプレイヤーの数字を選んでください")
        message_output_context.execute_output_message(f"0:{player1_name} 1:{player2_name}")
        first = int(input("数字 > "))

        # プレイヤー登録
        player1 = HumanPlayerFromTerminal(player1_color, player1_name)
        player2 = HumanPlayerFromTerminal(player2_color, player2_name)
        if(first == 0):
            player_manager.register_first_player(player1)
            player_manager.register_second_player(player2)
        else:
            player_manager.register_first_player(player2)
            player_manager.register_second_player(player1)

        # ゲーム開始
        message_output_context.execute_output_message("ゲームを開始します。")
        board_output_context.execute_output_board(board)
        now = 0

        # ゲーム進行
        while(1):
            # 終了判定
            result = processing.judge_result(board)
            if(result != -1): break

            # 石を置く
            if(now == 0):
                now_player = player_manager.first_player
            else:
                now_player = player_manager.second_player
            color = game_launcher_component.COLOR[now_player.color]
            name = now_player.name
            message_output_context.execute_output_message(f"{name}さんの番です。石({color})を置いてください。")
            board = now_player.put(board)
            sleep(0.3)
            board_output_context.execute_output_board(board)

            now = (now + 1) % 2
        
        # 結果発表
        result_output_context.execute_output(result)

class GameLauncherForHvConTerminal(GameLauncher):
    def play(self):
        # インスタンス化など前準備
        player_manager = PlayerManager()

        message_output = MessageOutputToTerminal()
        message_output_context = MessageOutputContext()
        message_output_context.set_message_output(message_output)

        processing = Processing()
        
        board = Board()
        board_output_context = BoardOutputContext()
        board_output_context.set_method(BoardOutputToTerminal())

        result_output_context = ResultOutputContext()
        result_output_context.set_method(ResultMessageOutput(player_manager, message_output))

        game_launcher_component = GameLauncherComponent()

        # 名前入力
        message_output_context.execute_output_message("あなたの名前を入力してください。")
        player1_name = str(input("> "))
        player2_name = "COM"

        # COMタイプ選択
        message_output_context.execute_output_message("対戦するコンピュータのタイプを選択してください。")
        message_output_context.execute_output_message(game_launcher_component.COM_INDEX)
        player2_comtype = int(input("> "))
        while(player2_comtype not in game_launcher_component.COM_CLASS.keys()):
            message_output_context.execute_output_message("選択した数字は不正です。選択しなおしてください。")
            player2_comtype = int(input("> "))
        
        # 石選択
        message_output_context.execute_output_message("白の石を使うプレイヤーの数字を選んでください。")
        message_output_context.execute_output_message(f"0:{player1_name} 1:{player2_name}")
        white = int(input("数字 > "))
        if(white == 0):
            player1_color = 0
            player2_color = 1
        else:
            player1_color = 1
            player2_color = 0
        
        # 先攻選択
        message_output_context.execute_output_message("先攻のプレイヤーの数字を選んでください")
        message_output_context.execute_output_message(f"0:{player1_name} 1:{player2_name}")
        first = int(input("数字 > "))

        # プレイヤー登録
        player1 = HumanPlayerFromTerminal(player1_color, player1_name)
        player2 = game_launcher_component.COM_CLASS[player2_comtype](player2_color, player2_name, message_output)
        if(first == 0):
            player_manager.register_first_player(player1)
            player_manager.register_second_player(player2)
        else:
            player_manager.register_first_player(player2)
            player_manager.register_second_player(player1)

        # ゲーム開始
        message_output_context.execute_output_message("ゲームを開始します。")
        board_output_context.execute_output_board(board)
        now = 0

        # ゲーム進行
        while(1):
            # 終了判定
            result = processing.judge_result(board)
            if(result != -1): break

            # 石を置く
            if(now == 0):
                now_player = player_manager.first_player
            else:
                now_player = player_manager.second_player
            color = game_launcher_component.COLOR[now_player.color]
            name = now_player.name
            message_output_context.execute_output_message(f"{name}さんの番です。石({color})を置いてください。")
            board = now_player.put(board)
            sleep(0.3)
            board_output_context.execute_output_board(board)

            now = (now + 1) % 2
        
        # 結果発表
        result_output_context.execute_output(result)

class GameLauncherOnGUI(GameLauncher):
    def play(self):
        GUIModeDesign()

class GameLauncherContext:
    def __init__(self):
        self.game_launcher = None

    def set_method(self, game_launcher: GameLauncher):
        self.game_launcher = game_launcher
    
    def execute_play(self):
        if self.game_launcher is not None:
            self.game_launcher.play()
        else:
            print("No method set up")

if __name__ == "__main__":
    game_launcher = GameLauncherOnGUI()
    game_launcher_context = GameLauncherContext()
    game_launcher_context.set_method(game_launcher)
    game_launcher_context.execute_play()