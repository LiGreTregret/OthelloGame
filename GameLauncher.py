from abc import ABC, abstractmethod
from MessageOutput import MessageOutputContext, MessageOutputToTerminal
from ModeSelector import ModeSelectorContext, \
                         ModeSelectorForHumanVsHumanOnTerminal as MSHvHT, \
                         ModeSelectorForVsComOnTerminal as MSvCT
from GameMode import GameModeContext, TerminalMode

class GameLauncher(ABC):
    @abstractmethod
    def play(self):
        pass

class GameLauncherForTerminal(GameLauncher):
    def play(self):
        # 定数
        MESSAGE = 0
        MODE_SELECTOR = 1
        GAME_MODE = 2

        # インスタンスの辞書
        instance_dict = {
            # ターミナルで2人プレイ
            0 : {MESSAGE :      MessageOutputToTerminal(),
                 MODE_SELECTOR: MSHvHT(),
                 GAME_MODE:     TerminalMode()},
            1 : {MESSAGE :      MessageOutputToTerminal(),
                 MODE_SELECTOR: MSvCT(),
                 GAME_MODE:     TerminalMode()}
        }

        # モード選択目次
        MODE_INDEX = (
            "0 : ターミナルで2人プレイ\n"
            "1 : ターミナルでCOMと対戦"
        )

        # メッセージだけ先にインスタンス化
        message_output_context = MessageOutputContext()
        message_output_context.set_message_output(instance_dict[0][MESSAGE])

        # モード選択
        message_output_context.execute_output_message("遊ぶゲームのモードを選択してください。")
        message_output_context.execute_output_message(MODE_INDEX)
        mode = int(input("> "))
        while(mode not in instance_dict.keys()):
            message_output_context.execute_output_message("選択した数字は不正です。選択しなおしてください。")
            message_output_context.execute_output_message("遊ぶゲームのモードを選択してください。")
            message_output_context.execute_output_message(MODE_INDEX)
            mode = int(input("> "))

        # 残り2つをインスタンス化
        mode_selector_context = ModeSelectorContext()
        game_mode_context = GameModeContext()

        # Strategy選択
        message_output_context.set_message_output(instance_dict[mode][MESSAGE])
        mode_selector_context.set_method(instance_dict[mode][MODE_SELECTOR])
        game_mode_context.set_mode(instance_dict[mode][GAME_MODE])

        # ゲーム進行
        mode_selector_context.execute_set_player()
        game_mode_context.execute_game(mode_selector_context.mode_selector.player_manager)

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
    game_launcher = GameLauncherForTerminal()
    game_launcher_context = GameLauncherContext()
    game_launcher_context.set_method(game_launcher)
    game_launcher_context.execute_play()