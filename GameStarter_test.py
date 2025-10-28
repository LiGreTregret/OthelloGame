from GameStarter import GameStarterForHvHonGUI, \
                        GameStarterForHvConGUI, \
                        GameStarterForCvConGUI

class GameSterterTest:
    def test_hvh(self):
        game_starter_hvh = GameStarterForHvHonGUI()

        player_dict = {
            game_starter_hvh.P1N : "White",
            game_starter_hvh.P2N : "Black",
            game_starter_hvh.P1C : 0,
            game_starter_hvh.P2C : 1
        }

        game_starter_hvh.start(player_dict)
    
    def test_hvc(self):
        game_starter_hvc = GameStarterForHvConGUI()

        player_dict = {
            game_starter_hvc.HN : "White",
            game_starter_hvc.CT : 3,
            game_starter_hvc.HC : 0,
            game_starter_hvc.CC : 1,
            game_starter_hvc.HO : 0
        }

        game_starter_hvc.start(player_dict)
    
    def test_cvc(self):
        game_starter_cvc = GameStarterForCvConGUI()

        player_dict = {
            game_starter_cvc.P1T : 1,
            game_starter_cvc.P2T : 2,
            game_starter_cvc.P1C : 0,
            game_starter_cvc.P2C : 1
        }

        game_starter_cvc.start(player_dict)

if __name__ == "__main__":
    game_starter_test = GameSterterTest()
    game_starter_test.test_hvc()