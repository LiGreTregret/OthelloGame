from src.board.processing import Processing
from src.board.board import Board
from collections import deque

class TestProcessing:
    def test_is_inside_board(self):
        processing = Processing()
        assert processing.is_inside_board(-1, -1) is False
        assert processing.is_inside_board(-1, 0) is False
        assert processing.is_inside_board(0, 0) is True
        assert processing.is_inside_board(7, 7) is True
        assert processing.is_inside_board(7, 8) is False
        assert processing.is_inside_board(8, 8) is False

    def test_is_blank(self):
        processing = Processing()
        board = Board()
        assert processing.is_blank(-1, -1, board) is False
        assert processing.is_blank(0, 0, board) is True
        assert processing.is_blank(3, 3, board) is False
        assert processing.is_blank(3, 4, board) is False
        assert processing.is_blank(7, 7, board) is True
        assert processing.is_blank(7, 8, board) is False

    def test_is_opponent(self):
        processing = Processing()
        board = Board()
        assert processing.is_opponent(-1, -1, 0, board) is False
        assert processing.is_opponent(0, 0, 0, board) is False
        assert processing.is_opponent(3, 3, 0, board) is False
        assert processing.is_opponent(3, 3, 1, board) is True
        assert processing.is_opponent(3, 4, 0, board) is True
        assert processing.is_opponent(8, 7, 0, board) is False

    def test_find_flippable_in_direction(self):
        processing = Processing()
        board = Board()

        processing.find_flippable_in_direction(4, 2, 0, 1, 0, board)
        assert processing.flippable_coordinates == deque([[4, 3]])

        processing.clear_flippable_coordinates()
        processing.find_flippable_in_direction(0, 0, -1, -1, 0, board)
        assert processing.flippable_coordinates == deque([])

        processing.find_flippable_in_direction(3, 5, 0, -1, 0, board)
        assert processing.flippable_coordinates == deque([[3, 4]])

        processing.clear_flippable_coordinates()
        processing.find_flippable_in_direction(5, 4, -1, 0, 1, board)
        assert processing.flippable_coordinates == deque([[4, 4]])
 
    def test_find_flippable(self):
        processing = Processing()
        board = Board()

        processing.find_flippable(4, 2, 0, board)
        assert processing.flippable_coordinates == deque([[4, 3]])

        processing.clear_flippable_coordinates()
        processing.find_flippable(0, 0, 0, board)
        assert processing.flippable_coordinates == deque([])

        processing.find_flippable(3, 5, 0, board)
        assert processing.flippable_coordinates == deque([[3, 4]])

        processing.clear_flippable_coordinates()
        processing.find_flippable(5, 4, 1, board)
        assert processing.flippable_coordinates == deque([[4, 4]])

    def test_is_valid_put(self):
        processing = Processing()
        board = Board()

        processing.find_flippable(4, 2, 0, board)
        assert processing.is_valid_put() == 1

        processing.clear_flippable_coordinates()
        processing.find_flippable(0, 0, 0, board)
        assert processing.is_valid_put() == 0

        processing.find_flippable(3, 5, 0, board)
        assert processing.is_valid_put() == 1

        processing.clear_flippable_coordinates()
        processing.find_flippable(5, 4, 1, board)
        assert processing.is_valid_put() == 1

    def test_put(self):
        processing = Processing()
        board = Board()

        board = processing.put(4, 2, 0, board)
        assert board.board[4][2] == 0
        board = processing.put(0, 0, 0, board)
        assert board.board[0][0] == 0
        board = processing.put(3, 5, 0, board)
        assert board.board[3][5] == 0
        board = processing.put(5, 4, 1, board)
        assert board.board[5][4] == 1

    def test_flip_one(self):
        processing = Processing()
        board = Board()

        board = processing.flip_one(3, 3, board)
        assert board.board[3][3] == 1
        board = processing.flip_one(3, 3, board)
        assert board.board[3][3] == 0
        board = processing.flip_one(0, 0, board)
        assert board.board[0][0] == -1
        board = processing.flip_one(4, 3, board)
        assert board.board[4][3] == 0

    def test_flip(self):
        processing = Processing()
        board = Board()

        processing.find_flippable(4, 2, 0, board)
        if(processing.is_valid_put()): board = processing.put(4, 2, 0, board)
        processing.flip(board)
        assert board.board[4][3] == 0

        processing.find_flippable(3, 2, 1, board)
        if(processing.is_valid_put()): board = processing.put(3, 2, 1, board)
        processing.flip(board)
        assert board.board[3][3] == 1

        saved_board = board.board
        processing.find_flippable(0, 0, 0, board)
        if(processing.is_valid_put()): board = processing.put(0, 0, 0, board)
        processing.flip(board)
        assert board.board == saved_board

    def test_judge_result(self):
        processing = Processing()
        board = Board()

        assert processing.judge_result(board) == -1
        board.board = [[0 for _ in range(8)] for _ in range(8)]
        assert processing.judge_result(board) == 0
        board.board = [[1 for _ in range(8)] for _ in range(8)]
        assert processing.judge_result(board) == 1
        board.board[0][0] = 0
        assert processing.judge_result(board) == 1
        board.board[0][0] = -1
        assert processing.judge_result(board) == 1
        board.board[0][1] = 0
        assert processing.judge_result(board) == -1
        
        for i in range(4):
            for j in range(8):
                board.board[i][j] = 0
        assert processing.judge_result(board) == 2

    def test_putable(self):
        processing = Processing()
        board = Board()
        assert processing.putable(0, board) == True
        board.board = [[0 for _ in range(8)] for _ in range(8)]
        assert processing.putable(1, board) == False
        board.board[0][0] = -1
        assert processing.putable(1, board) == False