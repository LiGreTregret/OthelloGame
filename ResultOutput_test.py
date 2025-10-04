from PlayerManager import PlayerManager as PM
from ResultOutput import ResultOutputContext, ResultOutputToTerminal
from Board import Board

class TestResultOutput:
    def test_result_output_to_terminal(self):
        player_manager = PM()
        player_manager.register_first_player(0, "White", PM.HUMAN_T)
        player_manager.register_second_player(1, "Black", PM.HUMAN_T)

        result_output_context = ResultOutputContext()
        result_output_context.set_method(ResultOutputToTerminal())

        # 「エラー」と出力
        result_output_context.execute_output(3, player_manager)

        # 「Whiteさんの勝ちです。」と出力
        result_output_context.execute_output(0, player_manager)

        # 「Blackさんの勝ちです。」と出力
        result_output_context.execute_output(1, player_manager)

        # 「同点です。」と出力
        result_output_context.execute_output(2, player_manager)


if __name__ == "__main__":
    test_result_output = TestResultOutput()
    test_result_output.test_result_output_to_terminal()