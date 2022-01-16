from distutils.log import error
import eel
import os
from utils import play_sound, pause_sounds, unpause_sounds, stop_sounds, set_volume, get_volume

eel.init('web')

@eel.expose
def stop_music():
    stop_sounds()


@eel.expose
def volume_info():
    return get_volume()

@eel.expose
def volume_mixer(vol):
    set_volume(vol)

@eel.expose
def next(path,sounds, atual):
    stop_sounds()
    idx = sounds.index(atual)
    idx_next = idx +1
    n = len(sounds)-1
    if idx_next >= n:
        play_sound(path+'\\'+sounds[0])
        return sounds[0]    
    else:
        play_sound(path+'\\'+sounds[idx_next])
        return sounds[idx_next]

@eel.expose
def prev(path,sounds, atual):
    stop_sounds()
    idx = sounds.index(atual)
    idx_prev = idx -1
    n = len(sounds)-1
    if idx_prev <= -1:
        play_sound(path+'\\'+sounds[-1])
        return sounds[-1]    
    else:
        play_sound(path+'\\'+sounds[idx_prev])
        return sounds[idx_prev]

                        
@eel.expose
def unpause():
    return unpause_sounds()

@eel.expose
def pause():
    return pause_sounds()

@eel.expose
def get_username():
    return os.environ.get('USERNAME')

@eel.expose
def get_musics(path):
    return [x for x in os.listdir(path) if '.mp3' in x or '.wav' in x or 'ogg' in x or 'wma' in x or 'aac' in x]

@eel.expose
def play(path,sounds):
    play_sound(path+'\\'+sounds[0])
    return sounds[0]


eel.start('index.html', size=(400,650))