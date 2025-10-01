from abc import ABC, abstractmethod
from PlayerManager import PlayerManager
from MessageOutput import MessageOutputContext, MessageOutputToTerminal

class ResultOutput(ABC):
    @abstractmethod

    def output_result(self, result, player_manager: PlayerManager):
        pass

class ResultOutputToTerminal(ResultOutput):
    def output_result(self, result, player_manager: PlayerManager):
        message_output_context = MessageOutputContext()
        message_output_context.set_message_output(MessageOutputToTerminal())

        if(player_manager.first_player.color == 0):
            player_names = [player_manager.first_player.name, player_manager.second_player.name]
        else:
            player_names = [player_manager.second_player.name, player_manager.first_player.name]

        # 出力
        if(result == 0):
            message_output_context.execute_output_message(f"{player_names[0]}さんの勝利です。")
        elif(result == 1):
            message_output_context.execute_output_message(f"{player_names[1]}さんの勝利です。")
        elif(result == 2):
            message_output_context.execute_output_message("引き分けです。")
        else:
            message_output_context.execute_output_message("エラー")

class ResultOutputContext:
    def __init__(self):
        self.result_output = None

    def set_method(self, result_output: ResultOutput):
        self.result_output = result_output
    
    def execute_output(self, result, player_manager: PlayerManager):
        if self.result_output is not None:
            self.result_output.output_result(result, player_manager)
        else:
            print("No method set up")