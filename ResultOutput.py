from abc import ABC, abstractmethod
from PlayerManager import PlayerManagerContext
from MessageOutput import MessageOutputContext, MessageOutputToTerminal

class ResultOutput(ABC):
    @abstractmethod

    def output_result(self, result, player_manager: PlayerManagerContext):
        pass

class ResultOutputToTerminal(ResultOutput):
    def output_result(self, result, player_manager_context: PlayerManagerContext):
        message_output_context = MessageOutputContext()
        message_output_context.set_message_output(MessageOutputToTerminal())

        # 出力文字列設定
        if(result == 0):
            message_output_context.execute_output_message(f"{player_manager_context.player_manager.first_player.name}さんの勝利です。")
        elif(result == 1):
            message_output_context.execute_output_message(f"{player_manager_context.player_manager.second_player.name}さんの勝利です。")
        elif(result == 2):
            message_output_context.execute_output_message("引き分けです。")
        else:
            message_output_context.execute_output_message("エラー")

class ResultOutputContext:
    def __init__(self):
        self.result_output = None

    def set_method(self, result_output: ResultOutput):
        self.result_output = result_output
    
    def execute_output(self, result, player_manager_context: PlayerManagerContext):
        if self.result_output is not None:
            self.result_output.output_result(result, player_manager_context)
        else:
            print("No method set up")