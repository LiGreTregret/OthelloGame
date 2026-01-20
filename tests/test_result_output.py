from src.player.player_manager import PlayerManager as PM
from src.player.player import HumanPlayerFromTerminal
from src.message.message_output import MessageOutputToTerminal, MessageOutputToGUI
from src.result.result_output import ResultOutputContext, ResultMessageOutput
from src.design.game_design import GUIGameDesign

class TestResultOutput:
    def test_result_output_to_terminal(self):
        player_manager = PM()

        first_player = HumanPlayerFromTerminal(0, "White")
        second_player = HumanPlayerFromTerminal(1, "Black")
        player_manager.register_first_player(first_player)
        player_manager.register_second_player(second_player)

        message_output = MessageOutputToTerminal()
        result_output = ResultMessageOutput(player_manager, message_output)

        result_output_context = ResultOutputContext()
        result_output_context.set_method(result_output)

        # 「エラー」と出力
        result_output_context.execute_output(3)

        # 「Whiteさんの勝ちです。」と出力
        result_output_context.execute_output(0)

        # 「Blackさんの勝ちです。」と出力
        result_output_context.execute_output(1)

        # 「同点です。」と出力
        result_output_context.execute_output(2)
    
    def test_result_output_to_gui(self):
        player_manager = PM()

        first_player = HumanPlayerFromTerminal(0, "White")
        second_player = HumanPlayerFromTerminal(1, "Black")
        player_manager.register_first_player(first_player)
        player_manager.register_second_player(second_player)

        gui_game_design = GUIGameDesign()

        message_output = MessageOutputToGUI(gui_game_design)
        result_output = ResultMessageOutput(player_manager, message_output)

        result_output_context = ResultOutputContext()
        result_output_context.set_method(result_output)

        # 「エラー」と出力
        result_output_context.execute_output(3)

        # 「Whiteさんの勝ちです。」と出力
        gui_game_design.root.after(1000, lambda: result_output_context.execute_output(0))

        # 「Blackさんの勝ちです。」と出力
        gui_game_design.root.after(2000, lambda: result_output_context.execute_output(1))

        # 「同点です。」と出力
        gui_game_design.root.after(3000, lambda: result_output_context.execute_output(2))

        gui_game_design.root.after(4000, gui_game_design.root.destroy)

        gui_game_design.root.mainloop()
        
if __name__ == "__main__":
    test_result_output = TestResultOutput()
    test_result_output.test_result_output_to_terminal()
    test_result_output.test_result_output_to_gui()