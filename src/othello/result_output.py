from abc import ABC, abstractmethod
from player_manager import PlayerManager
from message_output import MessageOutput, MessageOutputContext

class ResultOutput(ABC):
    @abstractmethod

    def __init__(self, player_manager: PlayerManager, message_output: MessageOutput):
        pass

    def output_result(self, result):
        pass

class ResultMessageOutput(ResultOutput):
    def __init__(self, player_manager: PlayerManager, message_output: MessageOutput):
        self.player_manager = player_manager
        self.message_output = message_output

    def output_result(self, result):
        message_output_context = MessageOutputContext()
        message_output_context.set_message_output(self.message_output)

        if(self.player_manager.first_player.order == 0):
            player_names = [self.player_manager.first_player.name, self.player_manager.second_player.name]
        else:
            player_names = [self.player_manager.second_player.name, self.player_manager.first_player.name]

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
    
    def execute_output(self, result):
        if self.result_output is not None:
            self.result_output.output_result(result)
        else:
            print("No method set up")