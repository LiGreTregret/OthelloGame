from Board import Board
from Processing import Processing
import tkinter as tk

class PutableHighlighter:
    def __init__(self, canvases):
        self.canvases = canvases
    
    def highlight(self, color, board: Board):
        processing = Processing()
        processing.find_putable(color, board)
        
        l = len(processing.putable_coordinates)
        for _ in range(l):
            putable_place = processing.putable_coordinates.pop()
            self.canvases[putable_place[0]][putable_place[1]].config(bg="yellow")
    
    def clear(self):
        for x in range(8):
            for y in range(8):
                self.canvases[x][y].config(bg="green")