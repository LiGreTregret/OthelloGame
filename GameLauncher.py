from MessageOutput import MessageOutputContext, MessageOutputToTerminal
from ModeSelector import ModeSelectorContext, ModeSelectorForHumanVsHumanOnTerminal
from GameMode import GameModeContext, TerminalMode

class GameLauncher:
    def play(self):
        # 定数
        MESSAGE = 0
        MODE_SELECTOR = 1
        GAME_MODE = 2

        # インスタンスの辞書
        instance_dict = {
            # ターミナルで2人プレイ
            0 : {MESSAGE :      MessageOutputToTerminal(),
                 MODE_SELECTOR: ModeSelectorForHumanVsHumanOnTerminal(),
                 GAME_MODE:     TerminalMode()}
        }

        # メッセージだけ先にインスタンス化
        message_output_context = MessageOutputContext()
        message_output_context.set_message_output(instance_dict[0][MESSAGE])

        # モード選択
        message_output_context.execute_output_message("遊ぶゲームのモードを選択してください。")
        message_output_context.execute_output_message("0 : ターミナルで2人プレイ")
        mode = int(input("> "))
        while(mode not in instance_dict.keys()):
            message_output_context.execute_output_message("選択した数字は不正です。選択しなおしてください。")
            message_output_context.execute_output_message("遊ぶゲームのモードを選択してください。")
            message_output_context.execute_output_message("0 : ターミナルで2人プレイ")
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
        game_mode_context.execute_game(mode_selector_context.mode_selector.player_manager_context.player_manager)

if __name__ == "__main__":
    game_launcher = GameLauncher()
    game_launcher.play()