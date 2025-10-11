import tkinter as tk
from MessageOutput import MessageOutputToTerminal, MessageOutputToGUI, MessageOutputContext
from time import sleep

# "Test"が出力されるか確認
class MessageOutputTest:
    def test_to_terminal(self):
        message_output_context = MessageOutputContext()
        message_output = MessageOutputToTerminal() # ここで出力方法を選択
        message_output_context.set_message_output(message_output)
        message_output_context.execute_output_message("Test")

    def test_to_gui(self):
        root = tk.Tk()
        root.title("MessageOutputToGUIのテスト")

        message_output_context = MessageOutputContext()
        message_output_gui = MessageOutputToGUI(root)
        message_output_context.set_message_output(message_output_gui)

        message_output_context.execute_output_message("Test")
        root.after(1000, lambda: message_output_context.execute_output_message("TEST", 1))
        root.mainloop()

if __name__ == "__main__":
    message_output_test = MessageOutputTest()
    message_output_test.test_to_terminal()
    message_output_test.test_to_gui()