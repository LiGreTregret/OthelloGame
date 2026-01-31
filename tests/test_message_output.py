from src.message.message_output import MessageOutputContext
from tests.mocks.dummy_message_output import DummyMessageOutputToTerminal, DummyMessageOutputToGUI
from tests.mocks.dummy_board import DummyGUIGameDesign

def test_to_terminal():
    message_output_context = MessageOutputContext()
    message_output = DummyMessageOutputToTerminal()

    message_output_context.set_message_output(message_output)

    message_output_context.execute_output_message("test_message_only")
    assert ("test_message_only", None, "") in message_output.calls

def test_to_gui():
    gui = DummyGUIGameDesign()

    message_output_context = MessageOutputContext()
    message_output = DummyMessageOutputToGUI(gui)
    message_output_context.set_message_output(message_output)

    message_output_context.execute_output_message("Test")
    assert message_output.label == "Test"
    message_output_context.execute_output_message("TEST", 1)
    gui.root.mainloop()
    assert message_output.label == "Test"
    assert ("TEST", 1, "Test") in message_output.calls 