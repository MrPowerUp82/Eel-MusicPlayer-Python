from distutils.log import error
import eel
import os
import sys
from utils import play_sound, pause_sounds, unpause_sounds, stop_sounds, set_volume, get_volume, get_art

eel.init('web')


@eel.expose
def art(path,sound):
    path_user = os.path.expanduser('~')
    if 'main.py' in sys.argv[0]:
        path_art = 'web\\'
        return get_art(path+'\\'+sound,path_art)
    else:
        path_art = f'{path_user}\\AppData\Local\\Temp\\pysound\\'
        path_art = path_art + os.listdir(path_art)[0]+'\\web\\'
        return get_art(path+'\\'+sound,path_art)

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
    username = os.environ.get('USERNAME')
    path_user = os.path.expanduser('~')
    system = sys.platform
    if system == 'win32':
        return [username,f'{path_user}\\Music']
    if (system == 'linux' or system == 'linux2') and username == 'root':
        return [username,f'/{username}/Music/']
    if system == 'linux' or system == 'linux2':
        return [username,f'/home/{username}/Music/']
    
    return 

@eel.expose
def get_musics(path):
    return [x for x in os.listdir(path) if '.mp3' in x or '.wav' in x or 'ogg' in x or 'wma' in x or 'aac' in x]

@eel.expose
def play(path,sounds):
    play_sound(path+'\\'+sounds[0])
    return sounds[0]


eel.start('index.html', size=(400,650))