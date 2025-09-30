from abc import ABC, abstractmethod
from MessageOutput import MessageOutputContext, MessageOutputToTerminal
from PlayerManager import PlayerManager
from Processing import Processing
from Board import Board, BoardOutputContext, BoardOutputToTerminal
from ResultOutput import ResultOutputContext, ResultOutputToTerminal

class GameMode(ABC):
    @abstractmethod
    def game(self, player_manager: PlayerManager):
        pass

class TerminalMode(GameMode):
    def game(self, player_manager: PlayerManager):
        message_output_context = MessageOutputContext()
        processing = Processing()
        board = Board()
        board_output_context = BoardOutputContext()
        result_output_context = ResultOutputContext()

        message_output_context.set_message_output(MessageOutputToTerminal())
        board_output_context.set_method(BoardOutputToTerminal())
        result_output_context.set_method(ResultOutputToTerminal())

        # 名前入力
        message_output_context.execute_output_message("先攻（白）の名前を入力してください。")
        first_player_name = str(input())
        player_manager.register_first_player(0, first_player_name)
        message_output_context.execute_output_message("後攻（黒）の名前を入力してください。")
        second_player_name = str(input())
        player_manager.register_second_player(1, second_player_name)

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
            name = now_player.name
            message_output_context.execute_output_message(f"{name}さんの番です。石を置いてください。")
            board = now_player.put(board)
            board_output_context.execute_output_board(board)

            now = (now + 1) % 2
        
        # 結果発表
        result_output_context.execute_output(result, player_manager)

class GameModeContext:
    def __init__(self):
        self.game_mode = None

    def set_mode(self, game_mode: GameMode):
        self.game_mode = game_mode
    
    def execute_game(self):
        if self.game_mode is not None:
            self.game_mode.game()
        else:
            print("No method set up")
