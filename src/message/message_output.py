from src.design.game_design import GUIGameDesign
from abc import ABC, abstractmethod

class MessageOutput(ABC):
    @abstractmethod
    def output_message(self, message, duration_s=None, current_text=None):
        pass

class MessageOutputToTerminal(MessageOutput):
    def output_message(self, message, duration_s=None, current_text=None):
        print(message)

class MessageOutputToGUI(MessageOutput):
    def __init__(self, gui_game_design: GUIGameDesign):
        self.label = gui_game_design.label

    def output_message(self, message, duration_s=None, current_text=""):
        if(current_text == ""):
            current_text = self.label.cget("text")
        self.label.config(text=message)
        if(duration_s is not None):
            self.label.after(int(duration_s*1000), lambda: self.label.config(text=current_text))

class MessageOutputContext:
    def __init__(self):
        self.message_output = None

    def set_message_output(self, message_output: MessageOutput):
        self.message_output = message_output
    
    def execute_output_message(self, message, duration_s=None, current_text=""):
        if self.message_output is not None:
            self.message_output.output_message(message, duration_s, current_text)
        else:
            print("No method set up")