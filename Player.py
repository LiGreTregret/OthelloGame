from abc import ABC, abstractmethod
from Board import Board
from Processing import Processing
from MessageOutput import MessageOutputContext, MessageOutputToTerminal
from time import sleep
import random

class Player(ABC):
    @abstractmethod
    def __init__(self, color, name):
        self.color = color
        self.name = name

    def put():
        pass

class HumanPlayerFromTerminal(Player):
    def __init__(self, color, name):
        super().__init__(color, name)
    
    def put(self, board: Board) -> Board:
        processing = Processing()
        message_output_context = MessageOutputContext()
        message_output_context.set_message_output(MessageOutputToTerminal())

        if(not(processing.putable(self.color, board))):
            message_output_context.execute_output_message("置ける場所がありません。")
            return board

        while(1):
            x, y = map(int, input("(上からx番目) (左からy番目) : ").split())
            x, y = x-1, y-1
            sleep(0.2)
            processing.find_flippable(x, y, self.color, board)
            if(processing.is_valid_put()):
                board = processing.put(x, y, self.color, board)
                board = processing.flip(board)
                break
            else:
                message_output_context.execute_output_message("そこには置けません。")
            sleep(0.2)
        return board
    
class RandomComputerPlayerFromTerminal(Player):
    def __init__(self, color, name):
        super().__init__(color, name)
    
    def put(self, board: Board) -> Board:
        processing = Processing()
        message_output_context = MessageOutputContext()
        message_output_context.set_message_output(MessageOutputToTerminal())

        processing.find_putable(self.color, board)
        l = len(processing.putable_coordinates)
        if(l == 0):
            message_output_context.execute_output_message("置ける場所がありません。")
            return board

        random.seed()
        select = random.randrange(l)
        for _ in range(select+1): place = processing.putable_coordinates.pop()
        x, y = place[0], place[1]
        sleep(0.2)
        processing.find_flippable(x, y, self.color, board)
        if(processing.is_valid_put()):
            board = processing.put(x, y, self.color, board)
            board = processing.flip(board)
        else:
            message_output_context.execute_output_message("そこには置けません。")
        sleep(0.2)
        
        return board

class MostComputerPlayerFromTerminal(Player):
    def __init__(self, color, name):
        super().__init__(color, name)
    
    def put(self, board: Board) -> Board:
        processing = Processing()
        message_output_context = MessageOutputContext()
        message_output_context.set_message_output(MessageOutputToTerminal())

        processing.find_putable(self.color, board)
        l = len(processing.putable_coordinates)
        if(l == 0):
            message_output_context.execute_output_message("置ける場所がありません。")
            return board

        m = [-1, -1, 0]
        for _ in range(l):
            c = processing.putable_coordinates.pop()
            if(c[2] > m[2]): m = c

        x, y = m[0], m[1]
        sleep(0.2)
        processing.find_flippable(x, y, self.color, board)
        if(processing.is_valid_put()):
            board = processing.put(x, y, self.color, board)
            board = processing.flip(board)
        else:
            message_output_context.execute_output_message("そこには置けません。")
        sleep(0.2)
        
        return board
    
class LeastComputerPlayerFromTerminal(Player):
    def __init__(self, color, name):
        super().__init__(color, name)
    
    def put(self, board: Board) -> Board:
        processing = Processing()
        message_output_context = MessageOutputContext()
        message_output_context.set_message_output(MessageOutputToTerminal())

        processing.find_putable(self.color, board)
        l = len(processing.putable_coordinates)
        if(l == 0):
            message_output_context.execute_output_message("置ける場所がありません。")
            return board

        m = [-1, -1, 100]
        for _ in range(l):
            c = processing.putable_coordinates.pop()
            if(c[2] < m[2]): m = c

        x, y = m[0], m[1]
        sleep(0.2)
        processing.find_flippable(x, y, self.color, board)
        if(processing.is_valid_put()):
            board = processing.put(x, y, self.color, board)
            board = processing.flip(board)
        else:
            message_output_context.execute_output_message("そこには置けません。")
        sleep(0.2)
        
        return board

class PlayerContext:
    def __init__(self):
        self.player = None

    def set_method(self, player: Player):
        self.player = player
    
    def execute_put(self, board: Board) -> Board:
        if self.player is not None:
            return self.player.put(board)
        else:
            print("No method set up")
            return board