from abc import ABC, abstractmethod
from Board import Board
from Processing import Processing
from MessageOutput import MessageOutputContext, MessageOutput, MessageOutputToTerminal, MessageOutputToGUI
from InputController import InputControllerGUI
from time import sleep
import random

class Player(ABC):
    @abstractmethod
    def put():
        pass

class HumanPlayerFromTerminal(Player):
    def __init__(self, color, name):
        self.color = color
        self.name = name
        self.message_output = MessageOutputToTerminal()
    
    def put(self, board: Board) -> Board:
        processing = Processing()
        message_output_context = MessageOutputContext()
        message_output_context.set_message_output(self.message_output)

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

class HumanPlayerFromGUI(Player):
    def __init__(self, color, name, input_controller: InputControllerGUI, frame_message, frame_board):
        self.color = color
        self.name = name
        self.input_controller = input_controller
        self.frame_message = frame_message
        self.frame_board = frame_board
        self.message_output = MessageOutputToGUI(frame_message)
    
    def put(self, board: Board) -> Board:
        processing = Processing()
        message_output_context = MessageOutputContext()
        message_output_context.set_message_output(self.message_output)

        if(not(processing.putable(self.color, board))):
            message_output_context.execute_output_message("置ける場所がありません。")
            return board

        while(1):
            x, y = self.input_controller.wait_for_click(self.frame_board)
            sleep(0.2)
            processing.find_flippable(x, y, self.color, board)
            if(processing.is_valid_put()):
                board = processing.put(x, y, self.color, board)
                board = processing.flip(board)
                break
            else:
                message_output_context.execute_output_message("そこには置けません。", 1)
            sleep(0.2)
        return board
    
class RandomComputerPlayer(Player):
    def __init__(self, color, name, message_output):
        self.color = color
        self.name = name
        self.message_output = message_output
    
    def put(self, board: Board) -> Board:
        processing = Processing()
        message_output_context = MessageOutputContext()
        message_output_context.set_message_output(self.message_output)

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

class MostComputerPlayer(Player):
    def __init__(self, color, name, message_output):
        self.color = color
        self.name = name
        self.message_output = message_output
    
    def put(self, board: Board) -> Board:
        processing = Processing()
        message_output_context = MessageOutputContext()
        message_output_context.set_message_output(self.message_output)

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
    
class LeastComputerPlayer(Player):
    def __init__(self, color, name, message_output):
        self.color = color
        self.name = name
        self.message_output = message_output
    
    def put(self, board: Board) -> Board:
        processing = Processing()
        message_output_context = MessageOutputContext()
        message_output_context.set_message_output(self.message_output)

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