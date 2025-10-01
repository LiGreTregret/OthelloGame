from PlayerManager import PlayerManagerContext, PlayerManagerForHumanVsHuman
from ResultOutput import ResultOutputContext, ResultOutputToTerminal
from Board import Board

class TestResultOutput:
    def test_result_output_to_terminal(self):
        player_manager_context = PlayerManagerContext()
        player_manager_context.set_method(PlayerManagerForHumanVsHuman())
        player_manager_context.execute_register_first_player(0, "White")
        player_manager_context.execute_register_second_player(1, "Black")

        result_output_context = ResultOutputContext()
        result_output_context.set_method(ResultOutputToTerminal())

        # 「エラー」と出力
        result_output_context.execute_output(3, player_manager_context.player_manager)

        # 「Whiteさんの勝ちです。」と出力
        result_output_context.execute_output(0, player_manager_context.player_manager)

        # 「Blackさんの勝ちです。」と出力
        result_output_context.execute_output(1, player_manager_context.player_manager)

        # 「同点です。」と出力
        result_output_context.execute_output(2, player_manager_context.player_manager)


if __name__ == "__main__":
    test_result_output = TestResultOutput()
    test_result_output.test_result_output_to_terminal()