from Player import PlayerContext, HumanPlayerFromTerminal
from Board import Board, BoardOutputContext, BoardOutputToTerminal

class TestPlayer:
    def test_put(self):
        player_context = PlayerContext()
        board = Board()
        board_output_context = BoardOutputContext()

        board_output_context.set_method(BoardOutputToTerminal())
        board_output_context.execute_output_board(board)
        
        player_context.set_method(HumanPlayerFromTerminal(0, 'White'))
        player_context.execute_put(board)

        board_output_context.execute_output_board(board)

if __name__ == '__main__':
    test_player = TestPlayer()
    test_player.test_put()