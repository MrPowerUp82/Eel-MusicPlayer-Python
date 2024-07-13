import eel
import os
import sys
from utils import get_art, get_time, search_for_musics
import tkinter 
import tkinter.filedialog as filedialog

eel.init('web')

ext_musics = ('mp3', 'wav','ogg','wma','aac')

@eel.expose
def select_path():
    root = tkinter.Tk()
    root.attributes("-topmost", True)
    root.withdraw()
    directory_path = filedialog.askdirectory()
    return directory_path+'/'

@eel.expose
def time_f(time):
    return get_time(time)[1]

@eel.expose
def start():
    return search_for_musics()

@eel.expose
def get_musics(path):
    music_list =[x for x in os.listdir(path) if x.endswith(ext_musics)]
    return music_list

@eel.expose
def create_file(music):
    ext = music.split('/')[-1].split('.')[-1]
    if 'main.py' in sys.argv[0]:
        path = os.getcwd()+'/web/'
    else:
        path =eel.root_path + '/'
    with open(f'{path}temp.{ext}', 'wb') as arq:
        music_arq = open(music, 'rb').read()
        arq.write(music_arq)

    art = get_art(music,path)

    return [f'temp.{ext}',ext,art]

eel.start('index.html', size=(400,625))

#Repack test