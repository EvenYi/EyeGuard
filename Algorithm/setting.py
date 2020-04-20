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
    
    
    HP_CODE = " "
    END = False
    STATUS_HP_END = False
    STATUS_EB_END = False
    STATUS_T = -1
    STATUS_HP = -1
    STATUS_EB = -1
    COUNTER = 0
    TOTAL = 0
    f = open('settings.txt', 'r')
    settings = f.read().split()
    IF_POP = settings[0]
    IF_MUSIC = settings[1]
    MUSIC_TYPE = settings[2]
    