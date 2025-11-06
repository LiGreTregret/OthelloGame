from abc import ABC, abstractmethod
from Board import Board
from Processing import Processing
from MessageOutput import MessageOutputContext, MessageOutput, MessageOutputToTerminal, MessageOutputToGUI
from InputController import InputControllerGUI
from GameDesign import GUIGameDesign
from PutableHighlighter import PutableHighlighter
import random
from copy import deepcopy

class Player(ABC):
    @abstractmethod
    def put():
        pass

class HumanPlayerFromTerminal(Player):
    def __init__(self, order, name, message_output: MessageOutput = MessageOutputToTerminal()):
        self.order = order
        self.name = name
        self.message_output = message_output
    
    def put(self, board: Board) -> Board:
        processing = Processing()
        message_output_context = MessageOutputContext()
        message_output_context.set_message_output(self.message_output)

        if(not(processing.putable(self.order, board))):
            message_output_context.execute_output_message("置ける場所がありません。")
            return board

        while(1):
            x, y = map(int, input("(上からx番目) (左からy番目) : ").split())
            x, y = x-1, y-1
            if(processing.is_blank(x, y, board)):
                processing.find_flippable(x, y, self.order, board)
            if(processing.is_valid_put()):
                board = processing.put(x, y, self.order, board)
                board = processing.flip(board)
                break
            else:
                message_output_context.execute_output_message("そこには置けません。")
        return board

class HumanPlayerFromGUI(Player):
    def __init__(self, order, name, input_controller: InputControllerGUI, gui_game_design: GUIGameDesign, message_output: MessageOutput):
        self.order = order
        self.name = name
        self.input_controller = input_controller
        self.frame_message = gui_game_design.frame_message
        self.frame_board = gui_game_design.frame_board
        self.message_output = message_output
    
    def put(self, board: Board) -> Board:
        processing = Processing()
        putable_highlighter = PutableHighlighter(self.frame_board)
        message_output_context = MessageOutputContext()
        message_output_context.set_message_output(self.message_output)

        if(not(processing.putable(self.order, board))):
            message_output_context.execute_output_message("置ける場所がありません。")
            return board

        putable_highlighter.highlight(self.order, board)
        while(1):
            x, y = self.input_controller.wait_for_click(self.frame_board)
            if(processing.is_blank(x, y, board)):
                processing.find_flippable(x, y, self.order, board)
            if(processing.is_valid_put()):
                board = processing.put(x, y, self.order, board)
                board = processing.flip(board)
                break
            else:
                message_output_context.execute_output_message("そこには置けません。", 1, f"{self.name}さんの番です。石を置いてください。")
        putable_highlighter.clear()
        return board
    
class RandomComputerPlayer(Player):
    def __init__(self, order, name, message_output):
        self.order = order
        self.name = name
        self.message_output = message_output
    
    def put(self, board: Board) -> Board:
        processing = Processing()
        message_output_context = MessageOutputContext()
        message_output_context.set_message_output(self.message_output)

        processing.find_putable(self.order, board)
        l = len(processing.putable_coordinates)
        if(l == 0):
            message_output_context.execute_output_message("置ける場所がありません。")
            return board

        random.seed()
        select = random.randrange(l)
        for _ in range(select+1): place = processing.putable_coordinates.pop()
        x, y = place[0], place[1]
        processing.find_flippable(x, y, self.order, board)
        if(processing.is_valid_put()):
            board = processing.put(x, y, self.order, board)
            board = processing.flip(board)
        else:
            message_output_context.execute_output_message("そこには置けません。", 1, f"{self.name}さんの番です。石を置いてください。")
        
        return board

class MostComputerPlayer(Player):
    def __init__(self, order, name, message_output):
        self.order = order
        self.name = name
        self.message_output = message_output
    
    def put(self, board: Board) -> Board:
        processing = Processing()
        message_output_context = MessageOutputContext()
        message_output_context.set_message_output(self.message_output)

        processing.find_putable(self.order, board)
        l = len(processing.putable_coordinates)
        if(l == 0):
            message_output_context.execute_output_message("置ける場所がありません。")
            return board

        m = [-1, -1, 0]
        for _ in range(l):
            c = processing.putable_coordinates.pop()
            if(c[2] > m[2]): m = c

        x, y = m[0], m[1]
        processing.find_flippable(x, y, self.order, board)
        if(processing.is_valid_put()):
            board = processing.put(x, y, self.order, board)
            board = processing.flip(board)
        else:
            message_output_context.execute_output_message("そこには置けません。", 1, f"{self.name}さんの番です。石を置いてください。")
        
        return board
    
class LeastComputerPlayer(Player):
    def __init__(self, order, name, message_output):
        self.order = order
        self.name = name
        self.message_output = message_output
    
    def put(self, board: Board) -> Board:
        processing = Processing()
        message_output_context = MessageOutputContext()
        message_output_context.set_message_output(self.message_output)

        processing.find_putable(self.order, board)
        l = len(processing.putable_coordinates)
        if(l == 0):
            message_output_context.execute_output_message("置ける場所がありません。")
            return board

        m = [-1, -1, 100]
        for _ in range(l):
            c = processing.putable_coordinates.pop()
            if(c[2] < m[2]): m = c

        x, y = m[0], m[1]
        processing.find_flippable(x, y, self.order, board)
        if(processing.is_valid_put()):
            board = processing.put(x, y, self.order, board)
            board = processing.flip(board)
        else:
            message_output_context.execute_output_message("そこには置けません。", 1, f"{self.name}さんの番です。石を置いてください。")
        
        return board

class LMComputerPlayer(Player):
    def __init__(self, order, name, message_output):
        self.order = order
        self.name = name
        self.message_output = message_output
    
    def put(self, board: Board) -> Board:
        processing = Processing()
        message_output_context = MessageOutputContext()
        message_output_context.set_message_output(self.message_output)
        lcp = LeastComputerPlayer(self.order, self.name, self.message_output)
        mcp = MostComputerPlayer(self.order, self.name, self.message_output)

        processing.find_putable(self.order, board)
        l = len(processing.putable_coordinates)
        if(l == 0):
            message_output_context.execute_output_message("置ける場所がありません。")
            return board
        
        num_blank = 0
        for i in range(8):
            for j in range(8):
                if(processing.is_blank(i, j, board)): num_blank += 1
        
        if(num_blank > 30): board = lcp.put(board)
        else: board = mcp.put(board)

        return board

class Lv1ComputerPlayer(Player):
    def __init__(self, order, name, message_output):
        self.order = order
        self.name = name
        self.message_output = message_output
    
    def is_corner(self, x, y) -> bool:
        if((x == 0 or x == 7) and (y == 0 or y == 7)):
            return True
        else:
            return False
    
    def risk_to_give_corner(self, x, y, board: Board):
        processing = Processing()
        board_buf = deepcopy(board)

        processing.find_flippable(x, y, self.order, board_buf)
        if not processing.is_valid_put():
            return False

        board_buf = processing.put(x, y, self.order, board_buf)
        board_buf = processing.flip(board_buf)

        opponent = (self.order + 1) % 2
        processing2 = Processing()
        processing2.find_putable(opponent, board_buf)
        putable_list = list(processing2.putable_coordinates)
        for v in putable_list:
            if self.is_corner(v[0], v[1]):
                return True
        return False
    
    def put(self, board: Board) -> Board:
        processing = Processing()
        message_output_context = MessageOutputContext()
        message_output_context.set_message_output(self.message_output)

        processing.find_putable(self.order, board)
        l = len(processing.putable_coordinates)
        if(l == 0):
            message_output_context.execute_output_message("置ける場所がありません。")
            return board

        m = [-1, -1, 100]
        for _ in range(l):
            c = processing.putable_coordinates.pop()
            if(c[2] < m[2]): m = c

        x, y = m[0], m[1]
        processing.find_flippable(x, y, self.order, board)
        if(processing.is_valid_put()):
            board = processing.put(x, y, self.order, board)
            board = processing.flip(board)
        else:
            message_output_context.execute_output_message("そこには置けません。", 1, f"{self.name}さんの番です。石を置いてください。")
        
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