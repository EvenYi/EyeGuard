import sys

sys.path.append(r'..\Algorithm')
import playsound
import setting


def p_audio():
    setting.STATUS_AU_END = True
    playsound.playsound('./' + setting.MUSIC_TYPE + '.mp3', True)
    setting.STATUS_AU_END = False
