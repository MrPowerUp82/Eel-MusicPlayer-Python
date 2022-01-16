from pygame import mixer

mixer.init()

def play_sound(path):
    mixer.music.load(path)
    mixer.music.play()


def stop_sounds():
    mixer.music.stop()
    
def pause_sounds():
    mixer.music.pause()
    
def unpause_sounds():
    mixer.music.unpause()
    
def is_sound_working():
    if mixer.music.get_busy() == True:
        return True
    
    return False

def get_volume():
    return mixer.music.get_volume()

def set_volume(vol):
    mixer.music.set_volume(vol)