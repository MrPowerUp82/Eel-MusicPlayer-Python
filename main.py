import eel
import os
import sys
from utils import get_art, get_time

eel.init('web')

@eel.expose
def time_f(time):
    return get_time(time)[1]

@eel.expose
def start():
    user_path = os.path.expanduser('~')
    return user_path+'/'+'Music'+'/'

@eel.expose
def get_musics(path):
    
    music_list =[x for x in os.listdir(path) if '.mp3' in x or '.wav' in x or 'ogg' in x or 'wma' in x or 'aac' in x]
    return music_list

@eel.expose
def create_file(music):
    ext = music.split('/')[-1].split('.')[-1]
    if 'main.py' in sys.argv[0]:
        path = os.getcwd()+'/web/'
    else:
        path = os.path.expanduser('~')+'/AppData/Local/Temp/pysound/'
        path =path+ os.listdir(path)[0]+'/web/'
    with open(f'{path}temp.{ext}', 'wb') as arq:
        music_arq = open(music, 'rb').read()
        arq.write(music_arq)

    art = get_art(music,path)

    return [f'temp.{ext}',ext,art]

eel.start('index.html', size=(400,625))