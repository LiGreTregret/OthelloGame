from abc import ABC, abstractmethod

class Board:
    def __init__(self):
        self.board = [[-1 for _ in range(8)] for _ in range(8)]
        self.board[3][3] = 0
        self.board[3][4] = 1
        self.board[4][3] = 1
        self.board[4][4] = 0
        

class BoardOutput(ABC):
    @abstractmethod
    def output_board(self, board: Board):
        pass

class BoardOutputToTerminal(BoardOutput):
    def output_board(self, board: Board):
        BLANK = ' '
        BLACK_STONE = '●'
        WHITE_STONE = '○'

        # 上枠
        print(" y12345678 ")
        print("x+--------+")

        for i in range(8):
            # 左枠
            print(f'{i+1}|', end='')
            
            # 中身
            buf = []
            for j in range(8):
                if board.board[i][j] == 1:
                    stone = BLACK_STONE
                elif board.board[i][j] == 0:
                    stone = WHITE_STONE
                else:
                    stone = BLANK
                buf.append(stone)
            print(*buf, sep='', end='')
            # 右枠
            print('|')
            
        # 下枠
        print(" +--------+")

class BoardOutputContext:
    def __init__(self):
        self.board_output_method = None

    def set_method(self, board_output_method: BoardOutput):
        self.board_output_method = board_output_method
    
    def execute_output_board(self, board: Board):
        if self.board_output_method is not None:
            self.board_output_method.output_board(board)
        else:
            print("No method set up")