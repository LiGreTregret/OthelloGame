from abc import ABC, abstractmethod
from PlayerManager import PlayerManagerContext, PlayerManagerForHumanVsHuman
from MessageOutput import MessageOutputContext, MessageOutputToTerminal

class ModeSelector(ABC):
    @abstractmethod
    def set_player(self):
        pass

class ModeSelectorForHumanVsHumanOnTerminal:
    def __init__(self):
        self.player_manager_context = PlayerManagerContext()

    def set_player(self):
        # インスタンス
        message_output_context = MessageOutputContext()
        self.player_manager_context.set_method(PlayerManagerForHumanVsHuman())
        message_output_context.set_message_output(MessageOutputToTerminal)

        # 名前入力
        message_output_context.execute_output_message("1人目の名前を入力してください。")
        player1_name = str(input())
        message_output_context.execute_output_message("2人目の名前を入力してください。")
        player2_name = str(input())
        
        # 石選択
        message_output_context.execute_output_message("白の石を使うプレイヤーの数字を選んでください。")
        message_output_context.execute_output_message(f"0:{player1_name} 1:{player2_name}")
        white = int(input())
        if(white == 0):
            player1_color = 0
            player2_color = 1
        else:
            player1_color = 1
            player2_color = 0
        
        # 先攻選択
        message_output_context("先攻のプレイヤーの数字を選んでください")
        message_output_context.execute_output_message(f"0:{player1_name} 1:{player2_name}")
        first = int(input())

        # プレイヤー登録
        if(first == 0):
            self.player_manager_context.execute_register_first_player(player1_color, player1_name)
            self.player_manager_context.execute_register_second_player(player2_color, player2_name)
        else:
            self.player_manager_context.execute_register_first_player(player2_color, player2_name)
            self.player_manager_context.execute_register_second_player(player1_color, player1_name)

class ModeSelectorContext:
    def __init__(self):
        self.mode_selector = None

    def set_method(self, mode_selector: ModeSelector):
        self.mode_selector = mode_selector
    
    def execute_set_player(self):
        if self.mode_selector is not None:
            self.mode_selector.set_player()
        else:
            print("No method set up")