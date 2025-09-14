from MessageOutput import MessageOutput, MessageOutputToTerminal, MessageOutputContext

# "Test"が出力されるか確認
class MessageOutputTest:
    def test(self):
        message_output_context = MessageOutputContext()
        message_output = MessageOutputToTerminal() # ここで出力方法を選択
        message_output_context.set_message_output(message_output)
        message_output_context.execute_output_message("Test")

if __name__ == "__main__":
    message_output_to_terminal_test = MessageOutputTest()
    message_output_to_terminal_test.test()