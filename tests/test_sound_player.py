from src.soundplay.sound_player import SoundPlayer

def test_play_sound():
    sound_player = SoundPlayer()

    sound_player.set_sound("sound/normal.mp3")

    sound_player.play_sound()