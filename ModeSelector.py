from PlayerManager import PlayerManagerContext, PlayerManagerForHumanVsHuman
from MessageOutput import MessageOutputContext

class ModeSelector:
    def __init__(self):
        self.player_manager_context = PlayerManagerContext()
    
    def set_player(self, player_manager_key):
        player_manager = {
            1 : PlayerManagerForHumanVsHuman()
        }

        self.player_manager_context.set_method(player_manager[player_manager_key])

        # 名前入力
        message_output_context = MessageOutputContext()
        message_output_context.execute_output_message("先攻（白）の名前を入力してください。")
        first_player_name = str(input())
        player_manager.register_first_player(0, first_player_name)
        message_output_context.execute_output_message("後攻（黒）の名前を入力してください。")
        second_player_name = str(input())
        player_manager.register_second_player(1, second_player_name)