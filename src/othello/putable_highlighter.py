from board import Board
from processing import Processing

class PutableHighlighter:
    def __init__(self, frame_board):
        self.frame_board = frame_board
    
    def highlight(self, color, board: Board):
        processing = Processing()
        processing.find_putable(color, board)
        
        l = len(processing.putable_coordinates)
        for _ in range(l):
            putable_place = processing.putable_coordinates.pop()
            canvas = self.frame_board.grid_slaves(row=putable_place[0], column=putable_place[1])[0]
            canvas.config(bg="yellow")
    
    def clear(self):
        for x in range(8):
            for y in range(8):
                canvas = self.frame_board.grid_slaves(row=x, column=y)[0]
                canvas.config(bg="green")