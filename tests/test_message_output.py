import tkinter as tk
from src.message.message_output import MessageOutputToTerminal, MessageOutputToGUI, MessageOutputContext
from src.design.game_design import GUIGameDesign

# "Test"が出力されるか確認
class MessageOutputTest:
    def test_to_terminal(self):
        message_output_context = MessageOutputContext()
        message_output = MessageOutputToTerminal() # ここで出力方法を選択
        message_output_context.set_message_output(message_output)
        message_output_context.execute_output_message("Test")

    def test_to_gui(self):
        gui_game_design = GUIGameDesign()

        message_output_context = MessageOutputContext()
        message_output_gui = MessageOutputToGUI(gui_game_design)
        message_output_context.set_message_output(message_output_gui)

        message_output_context.execute_output_message("Test")
        gui_game_design.root.after(1000, lambda: message_output_context.execute_output_message("TEST", 1))
        gui_game_design.root.mainloop()

if __name__ == "__main__":
    message_output_test = MessageOutputTest()
    message_output_test.test_to_terminal()
    message_output_test.test_to_gui()