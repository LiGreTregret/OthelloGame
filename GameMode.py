from abc import ABC, abstractmethod
from MessageOutput import MessageOutput, MessageOutputToTerminal, MessageOutputContext
from PlayerManager import PlayerManager
from Processing import Processing
from Board import Board, BoardOutput, BoardOutputToTerminal, BoardOutputContext
from ResultOutput import ResultOutputContext, ResultMessageOutput
from time import sleep

class GameMode(ABC):
    @abstractmethod
    def game(self, player_manager: PlayerManager):
        pass

class TerminalMode(GameMode):
    def game(self, player_manager: PlayerManager):
        processing = Processing()
        board = Board()

        board_output_context = BoardOutputContext()
        board_output_context.set_method(BoardOutputToTerminal())

        message_output = MessageOutputToTerminal()
        message_output_context = MessageOutputContext()
        message_output_context.set_message_output(message_output)

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
            sleep(0.3)
            board_output_context.execute_output_board(board)

            now = (now + 1) % 2
        
        # 結果発表
        result_output_context = ResultOutputContext()
        result_output_context.set_method(ResultMessageOutput(player_manager, message_output))
        result_output_context.execute_output(result)

class GUIMode(GameMode):
    def game(self, player_manager: PlayerManager):
        processing = Processing()
        board = Board()

        message_output = messageoutput
        message_output_context = MessageOutputContext()
        message_output_context.set_message_output(message_output)

        board_output_context = BoardOutputContext()
        board_output_context.set_method(board_output)

        def progress(result, now, message_output_context, board, board_output_context):
            # 終了判定
            result = processing.judge_result(board)
            if result != -1:
                result_output_context = ResultOutputContext()
                result_output_context.set_method(ResultMessageOutput(player_manager, message_output))
                result_output_context.execute_output(result)
                return
            
            # 石を置く
            if now == 0:
                now_player = player_manager.first_player
            else:
                now_player = player_manager.second_player

            name = now_player.name
            message_output_context.execute_output_message(f"{name}さんの番です。石を置いてください。")

            board = now_player.put(board)
            board_output.frame_board.after(500, lambda: board_output_context.execute_output_board(board))

            now = (now + 1) % 2

            board_output.frame_board.after(500, lambda: progress(result, now, message_output_context, board, board_output_context))

        board_output_context.execute_output_board(board)
        message_output_context.execute_output_message("ゲームを開始します。")
        board_output.frame_board.after(2000, lambda: progress(-1, 0, message_output_context, board, board_output_context))

class GameModeContext:
    def __init__(self):
        self.game_mode = None

    def set_mode(self, game_mode: GameMode):
        self.game_mode = game_mode
    
    def execute_game(self, player_manager: PlayerManager):
        if self.game_mode is not None:
            self.game_mode.game(player_manager)
        else:
            print("No method set up")