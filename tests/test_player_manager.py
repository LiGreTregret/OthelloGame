from src.player.player import (
    HumanPlayerFromTerminal as HPT,
    HumanPlayerFromGUI as HPG,
    RandomComputerPlayer as RCP,
    MostComputerPlayer as MCP,
    LeastComputerPlayer as LCP
)
from src.message.message_output import (
    MessageOutputToTerminal as MOT,
    MessageOutputToGUI as MOG
)
from src.controller.input_controller import InputControllerGUI as ICG
from src.player.player_manager import PlayerManager as PM
from src.design.game_design import GUIGameDesign
import tkinter as tk

class TestPlayerManager:
    def test_register_first_hpt(self):
        player = HPT(0, "White")
        player_manager = PM()

        player_manager.register_first_player(player)
        assert player_manager.first_player.order == 0
        assert player_manager.first_player.name == "White"
        
    def test_register_second_hpt(self):
        player = HPT(0, "White")
        player_manager = PM()

        player_manager.register_second_player(player)
        assert player_manager.second_player.order == 0
        assert player_manager.second_player.name == "White"
    
    def test_register_first_hpg(self):
        gui_game_design = GUIGameDesign()
        input_controller = ICG(gui_game_design)
        message_output = MOG(gui_game_design)
        
        player = HPG(0, "White", input_controller, gui_game_design, message_output)
        player_manager = PM()

        player_manager.register_first_player(player)
        assert player_manager.first_player.order == 0
        assert player_manager.first_player.name == "White"
        
    def test_register_second_hpg(self):
        gui_game_design = GUIGameDesign()
        input_controller = ICG(gui_game_design)
        message_output = MOG(gui_game_design)
        
        player = HPG(0, "White", input_controller, gui_game_design, message_output)
        player_manager = PM()

        player_manager.register_second_player(player)
        assert player_manager.second_player.order == 0
        assert player_manager.second_player.name == "White"
    
    def test_register_first_rcp(self):
        message_output = MOT()
        player = RCP(0, "White", message_output)
        player_manager = PM()

        player_manager.register_first_player(player)
        assert player_manager.first_player.order == 0
        assert player_manager.first_player.name == "White"
        assert player_manager.first_player.message_output == message_output
        
    def test_register_second_rcp(self):
        message_output = MOT()
        player = RCP(0, "White", message_output)
        player_manager = PM()

        player_manager.register_second_player(player)
        assert player_manager.second_player.order == 0
        assert player_manager.second_player.name == "White"
        assert player_manager.second_player.message_output == message_output
    
    def test_register_first_mcp(self):
        message_output = MOT()
        player = MCP(0, "White", message_output)
        player_manager = PM()

        player_manager.register_first_player(player)
        assert player_manager.first_player.order == 0
        assert player_manager.first_player.name == "White"
        assert player_manager.first_player.message_output == message_output
        
    def test_register_second_mcp(self):
        message_output = MOT()
        player = MCP(0, "White", message_output)
        player_manager = PM()

        player_manager.register_second_player(player)
        assert player_manager.second_player.order == 0
        assert player_manager.second_player.name == "White"
        assert player_manager.second_player.message_output == message_output
    
    def test_register_first_lcp(self):
        message_output = MOT()
        player = LCP(0, "White", message_output)
        player_manager = PM()

        player_manager.register_first_player(player)
        assert player_manager.first_player.order == 0
        assert player_manager.first_player.name == "White"
        assert player_manager.first_player.message_output == message_output
        
    def test_register_second_lcp(self):
        message_output = MOT()
        player = LCP(0, "White", message_output)
        player_manager = PM()

        player_manager.register_second_player(player)
        assert player_manager.second_player.order == 0
        assert player_manager.second_player.name == "White"
        assert player_manager.second_player.message_output == message_output