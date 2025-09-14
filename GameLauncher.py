from abc import ABC, abstractmethod
from MessageOutput import MessageOutputContext, MessageOutputToTerminal
from PlayerManager import PlayerManagerContext, PlayerManagerForHumanVsHumanOnTerminal 
from Processing import Processing
from Board import Board, BoardOutputContext, BoardOutputToTerminal

class GameLauncher(ABC):
    @abstractmethod
    def play(self):
        pass

class GameLauncherForHumanVsHumanOnTerminal(GameLauncher):
    def play(self):
        message_output_context = MessageOutputContext()
        player_manager_context = PlayerManagerContext()
        processing = Processing()
        board = Board()
        board_output_context = BoardOutputContext()

        message_output_context.set_message_output(MessageOutputToTerminal())
        player_manager_context.set_method(PlayerManagerForHumanVsHumanOnTerminal())
        board_output_context.set_method(BoardOutputToTerminal())

        # 名前入力
        message_output_context.execute_output_message("先攻（白）の名前を入力してください。")
        first_player_name = str(input())
        player_manager_context.execute_register_first_player(0, first_player_name)
        message_output_context.execute_output_message("後攻（黒）の名前を入力してください。")
        second_player_name = str(input())
        player_manager_context.execute_register_second_player(1, second_player_name)

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
                now_player = player_manager_context.player_manager.first_player
            else:
                now_player = player_manager_context.player_manager.second_player
            name = now_player.name
            message_output_context.execute_output_message(f"{name}さんの番です。石を置いてください。")
            board = now_player.put(board)
            board_output_context.execute_output_board(board)

            now = (now + 1) % 2
        
        # 結果発表
        if(result == 0):
            message_output_context.execute_output_message(f"{player_manager_context.player_manager.first_player.name}さんの勝利です。")
        elif(result == 1):
            message_output_context.execute_output_message(f"{player_manager_context.player_manager.second_player.name}さんの勝利です。")
        else:
            message_output_context.execute_output_message("引き分けです。")            

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
    game_launcher_context = GameLauncherContext()
    game_launcher_context.set_method(GameLauncherForHumanVsHumanOnTerminal())
    game_launcher_context.execute_play()