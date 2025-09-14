from PlayerManager import PlayerManagerContext, PlayerManagerForHumanVsHumanOnTerminal
from MessageOutput import MessageOutputContext, MessageOutputToTerminal
from ResultOutput import ResultOutputContext, ResultOutputToTerminal
from Board import Board

class TestResultOutput:
    def test_result_output_to_terminal(self):
        player_manager_context = PlayerManagerContext()
        player_manager_context.set_method(PlayerManagerForHumanVsHumanOnTerminal())
        player_manager_context.execute_register_first_player(0, "White")
        player_manager_context.execute_register_second_player(1, "Black")

        message_output_context = MessageOutputContext()
        message_output_context.set_message_output(MessageOutputToTerminal())

        result_output_context = ResultOutputContext()
        result_output_context.set_method(ResultOutputToTerminal())

        board = Board()

        # 「エラー」と出力
        result_output_context.execute_output(board, player_manager_context.player_manager, message_output_context.message_output)

        # 「Whiteさんの勝ちです。」と出力
        board.board = [[0 for _ in range(8)] for _ in range(8)]
        result_output_context.execute_output(board, player_manager_context.player_manager, message_output_context.message_output)

        # 「Blackさんの勝ちです。」と出力
        board.board = [[1 for _ in range(8)] for _ in range(8)]
        result_output_context.execute_output(board, player_manager_context.player_manager, message_output_context.message_output)

        # 「同点です。」と出力
        for i in range(4):
            for j in range(8):
                board.board[i][j] = 0
        result_output_context.execute_output(board, player_manager_context.player_manager, message_output_context.message_output)


if __name__ == "__main__":
    test_result_output = TestResultOutput()
    test_result_output.test_result_output_to_terminal()