from Player import (
    HumanPlayerFromTerminal as HPT,
    HumanPlayerFromGUI as HPG,
    RandomComputerPlayer as RCP,
    MostComputerPlayer as MCP,
    LeastComputerPlayer as LCP
)
from MessageOutput import MessageOutputToTerminal as MOT
from Board import BoardOutputToGUI
from InputController import InputControllerGUI as ICG
from PlayerManager import PlayerManager as PM
import tkinter as tk

class TestPlayerManager:
    def test_register_first_hpt(self):
        player = HPT(0, "White")
        player_manager = PM()

        player_manager.register_first_player(player)
        assert player_manager.first_player.color == 0
        assert player_manager.first_player.name == "White"
        
    def test_register_second_hpt(self):
        player = HPT(0, "White")
        player_manager = PM()

        player_manager.register_second_player(player)
        assert player_manager.second_player.color == 0
        assert player_manager.second_player.name == "White"
    
    def test_register_first_hpg(self):
        root = tk.Tk()
        frame_message = tk.Frame(root)
        frame_message.pack(side="top")
        frame_board = tk.Frame(root)
        frame_board.pack(side="bottom")

        board_output = BoardOutputToGUI(frame_board)

        input_controller = ICG(board_output.canvases)
        
        player = HPG(0, "White", input_controller, frame_message, frame_board)
        player_manager = PM()

        player_manager.register_first_player(player)
        assert player_manager.first_player.color == 0
        assert player_manager.first_player.name == "White"
        
    def test_register_second_hpg(self):
        root = tk.Tk()
        frame_message = tk.Frame(root)
        frame_message.pack(side="top")
        frame_board = tk.Frame(root)
        frame_board.pack(side="bottom")

        board_output = BoardOutputToGUI(frame_board)

        input_controller = ICG(board_output.canvases)
        
        player = HPG(0, "White", input_controller, frame_message, frame_board)
        player_manager = PM()

        player_manager.register_second_player(player)
        assert player_manager.second_player.color == 0
        assert player_manager.second_player.name == "White"
    
    def test_register_first_rcp(self):
        message_output = MOT()
        player = RCP(0, "White", message_output)
        player_manager = PM()

        player_manager.register_first_player(player)
        assert player_manager.first_player.color == 0
        assert player_manager.first_player.name == "White"
        assert player_manager.first_player.message_output == message_output
        
    def test_register_second_rcp(self):
        message_output = MOT()
        player = RCP(0, "White", message_output)
        player_manager = PM()

        player_manager.register_second_player(player)
        assert player_manager.second_player.color == 0
        assert player_manager.second_player.name == "White"
        assert player_manager.second_player.message_output == message_output
    
    def test_register_first_mcp(self):
        message_output = MOT()
        player = MCP(0, "White", message_output)
        player_manager = PM()

        player_manager.register_first_player(player)
        assert player_manager.first_player.color == 0
        assert player_manager.first_player.name == "White"
        assert player_manager.first_player.message_output == message_output
        
    def test_register_second_mcp(self):
        message_output = MOT()
        player = MCP(0, "White", message_output)
        player_manager = PM()

        player_manager.register_second_player(player)
        assert player_manager.second_player.color == 0
        assert player_manager.second_player.name == "White"
        assert player_manager.second_player.message_output == message_output
    
    def test_register_first_lcp(self):
        message_output = MOT()
        player = LCP(0, "White", message_output)
        player_manager = PM()

        player_manager.register_first_player(player)
        assert player_manager.first_player.color == 0
        assert player_manager.first_player.name == "White"
        assert player_manager.first_player.message_output == message_output
        
    def test_register_second_lcp(self):
        message_output = MOT()
        player = LCP(0, "White", message_output)
        player_manager = PM()

        player_manager.register_second_player(player)
        assert player_manager.second_player.color == 0
        assert player_manager.second_player.name == "White"
        assert player_manager.second_player.message_output == message_output