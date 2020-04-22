import configparser


def init():
    global COUNTER
    global TOTAL
    global vs
    global frame
    global rotation_vector
    global translation_vector
    global STATUS_T
    global END
    global HP_CODE
    global STATUS_EB
    global STATUS_EB_END
    global STATUS_HP
    global STATUS_HP_END
    global MUSIC_TYPE
    global IF_MUSIC
    global IF_POP
    global STATUS_T_END
    global EYE_AR_THRESH
    global EYE_AR_CONSEC_FRAMES
    global STATUS_AU
    global STATUS_AU_END
    global Camera
    global work_mode
    global mode

    HP_CODE = 0
    END = False
    STATUS_HP_END = False
    STATUS_EB_END = False
    STATUS_T_END = False
    STATUS_AU_END = False
    STATUS_HP = -1
    STATUS_EB = -1
    COUNTER = 0
    TOTAL = 0

    cf = configparser.ConfigParser()
    cf.read('./config.ini', encoding='utf-8')

    IF_POP = cf.getint("Remind-Mode", "IF_POP")
    IF_MUSIC = cf.getint("Remind-Mode", "IF_MUSIC")
    MUSIC_TYPE = cf.get("Remind-Mode", "MUSIC_TYPE")
    EYE_AR_THRESH = cf.getfloat("Threshold", "EYE_AR_THRESH")
    EYE_AR_CONSEC_FRAMES = cf.getfloat("Threshold", "EYE_AR_CONSEC_FRAMES")
    Camera = cf.getint("Mode", "Camera")
    work_mode = cf.getint("Mode", "work_mode")
