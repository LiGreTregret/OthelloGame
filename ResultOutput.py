from abc import ABC, abstractmethod
from Board import Board
from PlayerManager import PlayerManager
from MessageOutput import MessageOutput, MessageOutputContext, MessageOutputToTerminal
from Processing import Processing

class ResultOutput(ABC):
    @abstractmethod

    def output_result(self, board: Board, player_manager: PlayerManager):
        pass

class ResultOutputToTerminal(ResultOutput):
    def output_result(self, board: Board, player_manager: PlayerManager, message_output: MessageOutput):
        processing = Processing()
        winner = processing.judge_result(board)

        # 出力文字列設定
        if(player_manager.first_player.color == winner):
            result = player_manager.first_player.name + "さんの勝ちです。"
        elif(player_manager.second_player.color == winner):
            result = player_manager.second_player.name + "さんの勝ちです。"
        elif(winner == 2):
            result = "同点です。"
        else:
            result = "エラー"

        # 出力
        message_output_context = MessageOutputContext()
        message_output_context.set_message_output(MessageOutputToTerminal())
        message_output_context.execute_output_message(result)

class ResultOutputContext:
    def __init__(self):
        self.result_output = None

    def set_method(self, result_output: ResultOutput):
        self.result_output = result_output
    
    def execute_output(self, board: Board, player_manager: PlayerManager, message_output: MessageOutput):
        if self.result_output is not None:
            self.result_output.output_result(board, player_manager, message_output)
        else:
            print("No method set up")