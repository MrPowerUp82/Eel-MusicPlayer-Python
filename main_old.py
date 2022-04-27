import eel
import os
import sys
from utils import play_sound, pause_sounds, unpause_sounds, stop_sounds, set_volume, get_volume, get_art, get_pos, get_end, set_pos, is_working
import time
import threading

eel.init('web')

interrupt = False
idx = 0
music_list = []
path = ''


def pos_():
    while True:
        if eel._shutdown != None:
            exit()
        send = get_pos()
        send.append('pos')
        eel.general_pos(send)
        time.sleep(0.99)


def auto_next():
    global interrupt
    global idx
    global music_list
    global path

    working = is_working()
    while working:
        if eel._shutdown != None:
            exit()
        if interrupt:
            while interrupt:
                time.sleep(1)
        working = is_working()
        time.sleep(2.5)
       

    stop_sounds()
    idx_next = idx +1
    n = len(music_list)-1
    if idx_next > n:
        play_sound(path+'\\'+music_list[0])
        cover = art(path,music_list[0])
        eel.auto_next(music_list[0],path,cover)
        threading.Thread(target=auto_next).start()  
    else:
        play_sound(path+'\\'+music_list[idx_next])
        cover = art(path,music_list[idx_next])
        eel.auto_next(music_list[idx_next],path,cover)
        threading.Thread(target=auto_next).start()
    


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
    return set_pos(value)

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
    global idx
    global interrupt
    
    interrupt = True
    stop_sounds()
    idx = sounds.index(atual)
    idx_next = idx +1
    idx = idx_next
    n = len(sounds)-1
    if idx_next > n:
        play_sound(path+'\\'+sounds[0])
        interrupt = False
        return sounds[0]    
    else:
        play_sound(path+'\\'+sounds[idx_next])
        interrupt = False
        return sounds[idx_next]

@eel.expose
def prev(path,sounds, atual):
    global idx
    global interrupt
    
    interrupt = True
    stop_sounds()
    idx = sounds.index(atual)
    idx_prev = idx -1
    idx= idx_prev
    n = len(sounds)-1
    if idx_prev <= -1:
        play_sound(path+'\\'+sounds[-1])
        interrupt = False
        return sounds[-1]    
    else:
        play_sound(path+'\\'+sounds[idx_prev])
        interrupt = False
        return sounds[idx_prev]

                        
@eel.expose
def unpause():
    global interrupt
    
    interrupt = False
    return unpause_sounds()

@eel.expose
def pause():
    global interrupt
    interrupt = True
    return pause_sounds()

@eel.expose
def get_username():
    global path
    
    username = os.environ.get('USERNAME')
    path_user = os.path.expanduser('~')
    system = sys.platform
    if system == 'win32':
        path = f'{path_user}\\Music'
        return [username,f'{path_user}\\Music']
    if (system == 'linux' or system == 'linux2') and username == 'root':
        return [username,f'/{username}/Music/']
    if system == 'linux' or system == 'linux2':
        return [username,f'/home/{username}/Music/']
    
    return 

@eel.expose
def get_musics(path):
    global music_list
    
    music_list =[x for x in os.listdir(path) if '.mp3' in x or '.wav' in x or 'ogg' in x or 'wma' in x or 'aac' in x]
    return music_list

@eel.expose
def play(path,sounds):
    global idx
    
    play_sound(path+'\\'+sounds[idx])
    threading.Thread(target=auto_next).start()
    threading.Thread(target=pos_).start()
    return sounds[idx]


eel.start('index.html', size=(400,625))