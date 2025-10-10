import tkinter as tk
from abc import ABC, abstractmethod

class MessageOutput(ABC):
    @abstractmethod
    def output_message(self, message, duration_s=None):
        pass

class MessageOutputToTerminal(MessageOutput):
    def output_message(self, message, duration_s=None):
        print(message)

class MessageOutputToGUI(MessageOutput):
    def __init__(self, frame_message):
        self.label = tk.Label(frame_message, text="", font=("Arial", 10))
        self.label.pack(pady=5)
        self.default_text = ""

    def output_message(self, message, duration_s=None):
        self.label.config(text=message)
        if(duration_s is not None):
            self.label.after(duration_s*1000, lambda: self.label.config(text=self.default_text))

class MessageOutputContext:
    def __init__(self):
        self.message_output = None

    def set_message_output(self, message_output: MessageOutput):
        self.message_output = message_output
    
    def execute_output_message(self, message, duration_s=None):
        if self.message_output is not None:
            self.message_output.output_message(message, duration_s)
        else:
            print("No method set up")