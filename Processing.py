from Board import Board
from collections import deque

class Processing:
    def __init__(self):
        self.flippable_coordinates = deque()
        self.putable_coordinates = deque()

    def is_inside_board(self, x, y) -> bool:
        return ((0 <= x < 8) and (0 <= y < 8))
    
    def is_blank(self, x, y, board:Board) -> bool:
        if(self.is_inside_board(x, y)):
            return board.board[x][y] == -1
        else:
            return False

    def is_opponent(self, x, y, color, board:Board) -> bool:
        if(self.is_inside_board(x, y)):
            if(not(self.is_blank(x, y, board))):
                return board.board[x][y] + color == 1
        return False
    
    def find_flippable_in_direction(self, x, y, dx, dy, color, board:Board) -> None:
        stack = deque()
        flippable = False
        
        x += dx
        y += dy
        while(self.is_inside_board(x, y)):
            if(self.is_opponent(x, y, color, board)):
                stack.append([x, y])
            else: 
                if(board.board[x][y] == color):
                    flippable = True
                break
            x += dx
            y += dy
        
        if(flippable):
            while(len(stack)):
                self.flippable_coordinates.append(stack.popleft())
    
    def find_flippable(self, x, y, color, board:Board) -> None:
        dx = [1, 1, 0, -1, -1, -1, 0, 1]
        dy = [0, 1, 1, 1, 0, -1, -1, -1]
        for i in range(8): 
            self.find_flippable_in_direction(x, y, dx[i], dy[i], color, board)

    def is_valid_put(self) -> bool:
        return len(self.flippable_coordinates)
    
    def put(self, x, y, color, board:Board) -> Board: # 置けないときはもう1度置きなおしてもらうために、is_valid_put()とは別で
        if(0 <= color <= 1):
            board.board[x][y] = color
        return board
    
    def flip_one(self, x, y, board:Board):
        if(0 <= board.board[x][y] <= 1):
            board.board[x][y] = (board.board[x][y] + 1) % 2
        return board
    
    def flip(self, board:Board):
        while(len(self.flippable_coordinates)):
            stone = self.flippable_coordinates.popleft()
            x = stone[0]
            y = stone[1]
            self.flip_one(x, y, board)
        return board
    
    def judge_result(self, board:Board):
        stone = [0, 0]

        for i in range(8):
            for j in range(8):
                if(board.board[i][j] != -1):
                    stone[board.board[i][j]] += 1
        
        if(stone[0] + stone[1] == 64):
            if(stone[0] > stone[1]): return 0
            elif(stone[0] < stone[1]): return 1
            else: return 2
        else:   
            if(stone[0] == 0): return 1
            elif(stone[1] == 0): return 0
            else: return -1
    
    def clear_flippable_coordinates(self):
        self.flippable_coordinates.clear()

    def clear_putable_coordinates(self):
        self.putable_coordinates.clear()
    
    def find_putable(self, color, board:Board):
        for i in range(8):
            for j in range(8):
                if(board.board[i][j] == -1):
                    self.find_flippable(i, j, color, board)
                    num = len(self.flippable_coordinates)
                    if(num > 0): self.putable_coordinates.append([i, j, num])
                    self.clear_flippable_coordinates()

    def putable(self, color, board: Board):
        self.find_putable(color, board)
        l = len(self.putable_coordinates)
        self.clear_putable_coordinates()

        if(l): return True
        else: return False