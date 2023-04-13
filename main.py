import eel
import os
import sys
from utils import get_art, get_time, search_for_musics
import tkinter 
import tkinter.filedialog as filedialog

# if not sys.platform == 'win32':
#     actual_path = os.getcwd()
#     path = os.path.join('/tmp/')
#     os.chdir(path)
#     if not os.path.exists('pysound'):
#         os.mkdir('pysound')
    
#     os.chdir(actual_path)



eel.init('web')

ext_musics = [
    'mp3', 'wav','ogg','wma','aac']


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
    # user_path = os.path.expanduser('~')
    # path_music = [x for x in os.listdir(user_path) if 'Musi' in x or 'Músi' in x][0]
    # return user_path+'/'+(path_music if path_music else 'Music')+'/'

@eel.expose
def get_musics(path):
    music_list =[x for x in os.listdir(path) if x.split('.')[-1].lower() in ext_musics]
    return music_list

@eel.expose
def create_file(music):
    ext = music.split('/')[-1].split('.')[-1]
    if 'main.py' in sys.argv[0]:
        path = os.getcwd()+'/web/'
    else:
        # if sys.platform == 'win32':
        #     # path = os.path.expanduser('~')+'/AppData/Local/Temp/pysound/'
        #     path = os.path.join(temp_dir, 'pysound') + '/'
        # else:
        #     # if not os.path.exists('/tmp/pysound'):
        #     #     os.mkdir('/tmp/pysound')
        #     # path = '/tmp/pysound/'
        #     path = os.path.join(temp_dir, 'pysound') + '/'
        path =eel.root_path + '/'
    with open(f'{path}temp.{ext}', 'wb') as arq:
        music_arq = open(music, 'rb').read()
        arq.write(music_arq)

    art = get_art(music,path)

    return [f'temp.{ext}',ext,art]

eel.start('index.html', size=(400,625))

#Repack test