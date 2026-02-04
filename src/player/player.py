"""
プレイヤーの基底クラスと具象実装を定義するモジュール
- 抽象基底
    + Player
- 人間プレイヤー
    + HumanPlayerFromTerminal
    + HumanPlayerFromGUI
- コンピュータプレイヤー
    + RandomComputerPlayer
    + MostComputerPlayer
    + LeastComputerPlayer
    + LMComputerPlayer
    + Lv1ComputerPlayer
- 具象実装
    + PlayerContext
"""

from abc import ABC, abstractmethod
from src.board.board import Board
from src.board.processing import Processing
from src.message.message_output import MessageOutputContext, MessageOutput, MessageOutputToTerminal
from src.controller.input_controller import InputControllerGUI
from src.design.game_design import GUIGameDesign
from src.design.putable_highlighter import PutableHighlighter
from src.soundplay.sound_player import SoundPlayer, SoundIndex
import random

class Player(ABC):
    @abstractmethod
    def put():
        pass

class HumanPlayerFromTerminal(Player):
    def __init__(self, order, name, message_output: MessageOutput = MessageOutputToTerminal()):
        self.order = order
        self.name = name
        self.message_output = message_output
        self.record_manager = None

    def set_record_manager(self, record_manager) -> None:
        """対戦記録マネージャを設定する"""
        self.record_manager = record_manager
    
    def report_result(self, result: str) -> None:
        """対戦結果を記録する"""
        if self.record_manager is not None:
            self.record_manager.update_result(self.name, result)
    
    def put(self, board: Board) -> Board:
        """ターミナルから座標を受け取り石を置く"""
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
    def __init__(self, order, name, input_controller: InputControllerGUI, gui_game_design: GUIGameDesign, message_output: MessageOutput, sound: str = SoundIndex.SOUND_DICT[0][0]):
        self.order = order
        self.name = name
        self.input_controller = input_controller
        self.frame_message = gui_game_design.frame_message
        self.frame_board = gui_game_design.frame_board
        self.message_output = message_output
        self.record_manager = None
        self.sound_player = SoundPlayer()
        self.sound_player.set_sound(sound)
    
    def set_record_manager(self, record_manager) -> None:
        """対戦記録マネージャを設定する"""
        self.record_manager = record_manager
    
    def report_result(self, result: str) -> None:
        """対戦結果を記録する"""
        if self.record_manager is not None:
            self.record_manager.update_result(self.name, result)

    def put(self, board: Board) -> Board:
        """GUIから座標を受け取り石を置く"""
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
                self.sound_player.play_sound()
                break
            else:
                message_output_context.execute_output_message("そこには置けません。", 1, f"{self.name}さんの番です。石を置いてください。")
        putable_highlighter.clear()
        return board
    
class RandomComputerPlayer(Player):
    def __init__(self, order, name, message_output, sound: str = SoundIndex.SOUND_DICT[0][0]):
        self.order = order
        self.name = name
        self.message_output = message_output
        self.sound_player = SoundPlayer()
        self.sound_player.set_sound(sound)
    
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
            self.sound_player.play_sound()
        else:
            message_output_context.execute_output_message("そこには置けません。", 1, f"{self.name}さんの番です。石を置いてください。")
        
        return board

class MostComputerPlayer(Player):
    def __init__(self, order, name, message_output, sound: str = SoundIndex.SOUND_DICT[0][0]):
        self.order = order
        self.name = name
        self.message_output = message_output
        self.sound_player = SoundPlayer()
        self.sound_player.set_sound(sound)
    
    def put(self, board: Board) -> Board:
        processing = Processing()
        message_output_context = MessageOutputContext()
        message_output_context.set_message_output(self.message_output)

        processing.find_putable(self.order, board)
        l = len(processing.putable_coordinates)
        if(l == 0):
            message_output_context.execute_output_message("置ける場所がありません。")
            return board

        m = (-1, -1, 0)
        for _ in range(l):
            c = processing.putable_coordinates.pop()
            if(c[2] > m[2]): m = tuple(c)

        x, y = m[0], m[1]
        processing.find_flippable(x, y, self.order, board)
        if(processing.is_valid_put()):
            board = processing.put(x, y, self.order, board)
            board = processing.flip(board)
            self.sound_player.play_sound()
        else:
            message_output_context.execute_output_message("そこには置けません。", 1, f"{self.name}さんの番です。石を置いてください。")
        
        return board
    
class LeastComputerPlayer(Player):
    def __init__(self, order, name, message_output, sound: str = SoundIndex.SOUND_DICT[0][0]):
        self.order = order
        self.name = name
        self.message_output = message_output
        self.sound_player = SoundPlayer()
        self.sound_player.set_sound(sound)
    
    def put(self, board: Board) -> Board:
        processing = Processing()
        message_output_context = MessageOutputContext()
        message_output_context.set_message_output(self.message_output)

        processing.find_putable(self.order, board)
        l = len(processing.putable_coordinates)
        if(l == 0):
            message_output_context.execute_output_message("置ける場所がありません。")
            return board

        m = (-1, -1, 100)
        for _ in range(l):
            c = processing.putable_coordinates.pop()
            if(c[2] < m[2]): m = tuple(c)

        x, y = m[0], m[1]
        processing.find_flippable(x, y, self.order, board)
        if(processing.is_valid_put()):
            board = processing.put(x, y, self.order, board)
            board = processing.flip(board)
            self.sound_player.play_sound()
        else:
            message_output_context.execute_output_message("そこには置けません。", 1, f"{self.name}さんの番です。石を置いてください。")
        
        return board

class LMComputerPlayer(Player):
    def __init__(self, order, name, message_output, sound: str = SoundIndex.SOUND_DICT[0][0]):
        self.order = order
        self.name = name
        self.message_output = message_output
        self.sound = sound
    
    def put(self, board: Board) -> Board:
        processing = Processing()
        message_output_context = MessageOutputContext()
        message_output_context.set_message_output(self.message_output)
        lcp = LeastComputerPlayer(self.order, self.name, self.message_output, self.sound)
        mcp = MostComputerPlayer(self.order, self.name, self.message_output, self.sound)

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
    def __init__(self, order, name, message_output, sound: str = SoundIndex.SOUND_DICT[0][0]):
        self.order = order
        self.name = name
        self.message_output = message_output
        self.sound_player = SoundPlayer()
        self.sound_player.set_sound(sound)
    
    def is_corner(self, x, y) -> bool:
        if((x == 0 or x == 7) and (y == 0 or y == 7)):
            return True
        else:
            return False
    
    def select_least(self, board: Board):
        processing = Processing()
        message_output_context = MessageOutputContext()
        message_output_context.set_message_output(self.message_output)

        processing.find_putable(self.order, board)
        l = len(processing.putable_coordinates)
        if(l == 0):
            message_output_context.execute_output_message("置ける場所がありません。")
            return board

        m = (-1, -1, 100)
        found_corner = False
        for _ in range(l):
            c = processing.putable_coordinates.pop()
            if(self.is_corner(c[0], c[1])):
                if(found_corner):
                    if(c[2] < m[2]): m = tuple(c)
                else:
                    m = tuple(c)
                    found_corner = True
            else:
                if(not(found_corner)):
                    if(c[2] < m[2]): m = tuple(c)

        x, y = m[0], m[1]
        processing.find_flippable(x, y, self.order, board)
        if(processing.is_valid_put()):
            board = processing.put(x, y, self.order, board)
            board = processing.flip(board)
        else:
            message_output_context.execute_output_message("そこには置けません。", 1, f"{self.name}さんの番です。石を置いてください。")
        
        return board
    
    def select_most(self, board: Board):
        processing = Processing()
        message_output_context = MessageOutputContext()
        message_output_context.set_message_output(self.message_output)

        processing.find_putable(self.order, board)
        l = len(processing.putable_coordinates)
        if(l == 0):
            message_output_context.execute_output_message("置ける場所がありません。")
            return board

        m = (-1, -1, 0)
        found_corner = False
        for _ in range(l):
            c = processing.putable_coordinates.pop()
            if(self.is_corner(c[0], c[1])):
                if(found_corner):
                    if(c[2] > m[2]): m = tuple(c)
                else:
                    m = tuple(c)
                    found_corner = True
            else:
                if(not(found_corner)):
                    if(c[2] > m[2]): m = tuple(c)

        x, y = m[0], m[1]
        processing.find_flippable(x, y, self.order, board)
        if(processing.is_valid_put()):
            board = processing.put(x, y, self.order, board)
            board = processing.flip(board)
            self.sound_player.play_sound()
        else:
            message_output_context.execute_output_message("そこには置けません。", 1, f"{self.name}さんの番です。石を置いてください。")
        
        return board
    
    def put(self, board: Board) -> Board:
        processing = Processing()

        num_blank = 0
        for i in range(8):
            for j in range(8):
                if(processing.is_blank(i, j, board)): num_blank += 1
        
        if(num_blank > 30): board = self.select_least(board)
        else: board = self.select_most(board)

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
        
class ComputerIndex:
    COM_TYPE = {
        0 : [RandomComputerPlayer, "ランダム"],
        1 : [MostComputerPlayer, "最多選択"],
        2 : [LeastComputerPlayer, "最少選択"],
        3 : [LMComputerPlayer, "少から多"],
        4 : [Lv1ComputerPlayer, "Lv.1"]
    }