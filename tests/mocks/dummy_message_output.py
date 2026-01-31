from src.message.message_output import MessageOutput
from tests.mocks.dummy_board import DummyGUIGameDesign

class DummyMessageOutputToTerminal(MessageOutput):
    def __init__(self):
        self.calls = []

    def output_message(self, message, duration_s=None, current_text=None):
        self.calls.append((message, duration_s, current_text))

class DummyMessageOutputToGUI(MessageOutput):
    def __init__(self, gui: DummyGUIGameDesign):
        self.label = gui.label
        self.calls = []

    def output_message(self, message, duration_s=None, current_text=""):
        if(current_text == ""):
            current_text = self.label
        self.label = message
        if(duration_s is not None):
            self.label = current_text
            self.calls.append((message, duration_s, current_text))