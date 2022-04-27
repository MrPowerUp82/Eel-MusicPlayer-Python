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

    
def get_end(file):
    meta = audio_metadata.load(file)['streaminfo']['duration']
    time =  strftime("%M:%S", gmtime(int(meta)))
    return [meta,time]
    

def get_time(timer):
    time =  strftime("%M:%S", gmtime(int(timer)))
    return [timer, time]

