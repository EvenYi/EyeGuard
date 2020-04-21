import sys

sys.path.append(r'.\Algorithm')
sys.path.append(r'.\Behavior')
sys.path.append(r'.\OperatingSystem')
from imutils.video import VideoStream
import threading
import setting
from facedetection import facedetection_background
import MainUI

def main():
    setting.init()
    # grab the indexes of the facial landmarks

    print("[INFO] Starting video stream thread...")
    setting.vs = VideoStream(src=setting.Camera).start()
    facedetection = threading.Thread(target=facedetection_background, name='Face')
    facedetection.start()
    MainUI.main_ui()
    setting.vs.stop()
    print("[INFO] Stop video thread...")
    print("[INFO] Exit")
    sys.exit(1)


if __name__ == '__main__':  # 在win系统下必须要满足这个if条件
    main()
