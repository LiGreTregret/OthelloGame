from abc import ABC, abstractmethod

class MessageOutput(ABC):
    @abstractmethod
    def output_message(message):
        pass

class MessageOutputToTerminal(MessageOutput):
    def output_message(self, message):
        print(message)

class MessageOutputContext:
    def __init__(self):
        self.message_output = None

    def set_message_output(self, message_output: MessageOutput):
        self.message_output = message_output
    
    def execute_output_message(self, message):
        if self.message_output is not None:
            self.message_output.output_message(message)
        else:
            print("No method set up")