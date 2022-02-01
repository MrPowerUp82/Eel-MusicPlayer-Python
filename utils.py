import threading
from pygame import mixer
import audio_metadata
from time import strftime
from time import gmtime


def get_art(sound,path_art):
    metadata = audio_metadata.load(sound)
    try:
        art = metadata.pictures[0].data
    except:
        return 'img.jpg'
    with open(f'{path_art}temp_art.png', 'wb') as arq:
        arq.write(art)
    return f'temp_art.png'

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
    
def get_volume():
    return mixer.music.get_volume()

def set_volume(vol):
    return mixer.music.set_volume(vol)
    
def get_pos():
    time_int = mixer.music.get_pos()/1000
    time = strftime("%M:%S", gmtime(int(time_int)))
    return [time_int,time]
    
def get_end(file):
    meta = audio_metadata.load(file)['streaminfo']['duration']
    time =  strftime("%M:%S", gmtime(int(meta)))
    return [meta,time]
    
def set_pos(value):
    mixer.music.set_pos(value)
    return False


def get_time(x):
    time =  strftime("%M:%S", gmtime(int(x)))
    return [x,time]

def is_working():
    return mixer.music.get_busy()