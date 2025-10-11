from abc import ABC, abstractmethod
from PlayerManager import PlayerManager
from Player import HumanPlayerFromTerminal, RandomComputerPlayer, MostComputerPlayer, LeastComputerPlayer
from MessageOutput import MessageOutputContext, MessageOutputToTerminal

class ModeSelector(ABC):
    @abstractmethod
    def set_player(self):
        pass

class ModeSelectorForHumanVsHumanOnTerminal(ModeSelector):
    def __init__(self):
        self.player_manager = PlayerManager()
        self.message_output = MessageOutputToTerminal()

    def set_player(self):
        # インスタンス
        message_output_context = MessageOutputContext()
        message_output_context.set_message_output(self.message_output)

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
            self.player_manager.register_first_player(player1)
            self.player_manager.register_second_player(player2)
        else:
            self.player_manager.register_first_player(player2)
            self.player_manager.register_second_player(player1)

class ModeSelectorForVsComOnTerminal(ModeSelector):
    def __init__(self):
        self.player_manager = PlayerManager()

    def set_player(self):
        # インスタンス
        message_output = MessageOutputToTerminal()
        message_output_context = MessageOutputContext()
        message_output_context.set_message_output(message_output)

        # 名前入力
        message_output_context.execute_output_message("あなたの名前を入力してください。")
        player1_name = str(input("> "))
        player2_name = "COM"

        # COMタイプ選択
        COM_INDEX = (
            "0 : ランダム\n"
            "1 : 1番多くひっくり返せる場所に置く\n"
            "2 : 1番少なくひっくり返せる場所に置く"
        )

        COM_CLASS = {
            0 : RandomComputerPlayer,
            1 : MostComputerPlayer,
            2 : LeastComputerPlayer
        }

        message_output_context.execute_output_message("対戦するコンピュータのタイプを選択してください。")
        message_output_context.execute_output_message(COM_INDEX)
        player2_comtype = int(input("> "))
        while(player2_comtype not in COM_CLASS.keys()):
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
        player2 = COM_CLASS[player2_comtype](player2_color, player2_name, message_output)
        if(first == 0):
            self.player_manager.register_first_player(player1)
            self.player_manager.register_second_player(player2)
        else:
            self.player_manager.register_first_player(player2)
            self.player_manager.register_second_player(player1)

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