import audio_metadata
from time import strftime
from time import gmtime
import os
from functools import lru_cache
from unicodedata import normalize

ext_musics = ('mp3', 'wav','ogg','wma','aac')

def tirar_acento(text):
    clean_text = normalize('NFKD',text).encode('ASCII','ignore').decode('ASCII')
    return clean_text

@lru_cache
def search_for_musics()->str:
    user_path = os.path.expanduser('~')
    possibles_dirs = [user_path+'/'+x for x in os.listdir(user_path) if os.path.isdir(user_path+'/'+x) and (tirar_acento(x).lower().startswith('downloa') or tirar_acento(x).lower().startswith('music'))]
    for possible_dir in possibles_dirs:
        for root, dir, files in os.walk(possible_dir):
            if any([x for x in root.split(os.path.sep) if x.startswith('.')]): continue
            if len([x for x in files if x == 'temp.mp3']): continue
            if len([x for x in files if x.endswith(ext_musics)]): return root + '/'

    return user_path

def get_art(sound,path_art):
    try:
        metadata = audio_metadata.load(sound)
        art = metadata.pictures[0].data
    except:
        return 'img.jpg'
    with open(f'{path_art}temp_art.png', 'wb') as arq:
        arq.write(art)
    return f'temp_art.png'
    
def get_end(file):
    meta = audio_metadata.load(file)['streaminfo']['duration']
    time =  strftime("%M:%S", gmtime(int(meta)))
    return [meta,time]

def get_time(timer):
    time =  strftime("%M:%S", gmtime(int(timer)))
    return [timer, time]

