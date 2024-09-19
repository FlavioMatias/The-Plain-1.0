from pygame import mixer
mixer.init()

music_state = ""
volume_E = 3
volume_M = 5

damage_sound = mixer.Sound("aud/dano-sound.wav")
button_sound = mixer.Sound("aud/button.wav")
atk_sound = mixer.Sound("aud/attack.wav")
lose_sound = mixer.Sound("aud/derrota.wav")
win_sound = mixer.Sound("aud/win.wav")


