import eel
import os
import sys
import threading
import time
from utils import play_sound, pause_sounds, unpause_sounds, stop_sounds, set_volume, get_volume, get_art, get_pos, get_end, set_pos, get_time

eel.init('web')

interrupt = False
timer_ = 1

def pos_():
    global interrupt

    global timer_

    while not interrupt:
        send = get_time(timer_)
        send.append('pos')
        eel.general_pos(send)
        time.sleep(1)
        if eel._shutdown != None:
            exit()
        timer_+=1


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
def def_pos(value):
    global interrupt
    global timer_

    if interrupt:
        timer_ = value
        send = get_time(timer_)
        send.append('pos')
        eel.general_pos(send)
        return set_pos(value)

    interrupt = True
    timer_ = value
    set_pos(value)
    interrupt = False
    threading.Thread(target=pos_).start()

@eel.expose
def music_pos():
   return get_pos() 

@eel.expose
def stop_music():
    global interrupt

    interrupt = True
    stop_sounds()

@eel.expose
def end_music(path,sounds):
    file = path+'\\'+sounds
    return get_end(file)

@eel.expose
def volume_info():
    return get_volume()

@eel.expose
def volume_mixer(vol):
    set_volume(vol)

@eel.expose
def next(path,sounds, atual):
    global interrupt
    global timer_

    interrupt = True
    timer_ = 1
    stop_sounds()
    idx = sounds.index(atual)
    idx_next = idx +1
    n = len(sounds)-1
    if idx_next > n:
        play_sound(path+'\\'+sounds[0])
        interrupt = False
        threading.Thread(target=pos_).start()
        return sounds[0]    
    else:
        play_sound(path+'\\'+sounds[idx_next])
        interrupt = False
        threading.Thread(target=pos_).start()
        return sounds[idx_next]

@eel.expose
def prev(path,sounds, atual):
    global interrupt
    global timer_

    interrupt = True
    timer_ = 1
    stop_sounds()
    idx = sounds.index(atual)
    idx_prev = idx -1
    n = len(sounds)-1
    if idx_prev <= -1:
        play_sound(path+'\\'+sounds[-1])
        threading.Thread(target=pos_).start()
        return sounds[-1]
    else:
        play_sound(path+'\\'+sounds[idx_prev])
        threading.Thread(target=pos_).start()
        return sounds[idx_prev]

                        
@eel.expose
def unpause():
    global interrupt

    interrupt = False
    threading.Thread(target=pos_).start()
    return unpause_sounds()

@eel.expose
def pause():
    global interrupt

    interrupt = True
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
    threading.Thread(target=pos_).start()
    return sounds[0]


eel.start('index.html', size=(400,625))