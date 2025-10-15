from abc import ABC, abstractmethod
from Design import GUIGameDesign
import tkinter as tk

class Board:
    def __init__(self):
        self.board = [[-1 for _ in range(8)] for _ in range(8)]
        self.board[3][3] = 0
        self.board[3][4] = 1
        self.board[4][3] = 1
        self.board[4][4] = 0

###########################################################################

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

        for x in range(8):
            # 左枠
            print(f'{x+1}|', end='')
            
            # 中身
            buf = []
            for y in range(8):
                if board.board[x][y] == 1:
                    stone = BLACK_STONE
                elif board.board[x][y] == 0:
                    stone = WHITE_STONE
                else:
                    stone = BLANK
                buf.append(stone)
            print(*buf, sep='', end='')
            # 右枠
            print('|')
            
        # 下枠
        print(" +--------+")

class BoardOutputToGUI(BoardOutput):
    def __init__(self, gui_game_design: GUIGameDesign):
        self.canvases = gui_game_design.canvases
        self.cell_size = gui_game_design.cell_size

    def draw_stone(self, x, y, color):
        c = self.canvases[x][y]
        margin = 5
        c.create_oval(
            margin, margin, 
            self.cell_size-margin, self.cell_size-margin,
            fill=color
        )
    
    def output_board(self, board: Board):
        for x in range(8):
            for y in range(8):
                c = self.canvases[x][y]
                c.delete("stone")
                value = board.board[x][y]
                if(value == 1):
                    self.draw_stone(x, y, "black")
                elif(value == 0):
                    self.draw_stone(x, y, "white")

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