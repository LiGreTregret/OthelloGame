from ModeSelector import ModeSelectorContext, ModeSelectorForHumanVsHumanOnTerminal

class TestModeSelector:
    def t_set_player(self):
        mode_selector_context = ModeSelectorContext()
        mode_selector_context.set_method(ModeSelectorForHumanVsHumanOnTerminal())
        mode_selector_context.execute_set_player()
        first_player = mode_selector_context.mode_selector.player_manager.first_player
        second_player = mode_selector_context.mode_selector.player_manager.second_player
        print(f"first: {first_player.color}, {first_player.name}")
        print(f"second: {second_player.color}, {second_player.name}")

if __name__ == "__main__":
    test_mode_selector = TestModeSelector()
    test_mode_selector.t_set_player()