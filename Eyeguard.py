import sys

sys.path.append(r'.\Algorithm')
sys.path.append(r'.\Behavior')
sys.path.append(r'.\OperatingSystem')
from imutils.video import VideoStream
import threading
import time
import setting
from facedetection import facedetection_background
import MainUI
import inspect
import ctypes


def _async_raise(tid, exctype):
    """raises the exception, performs cleanup if needed"""
    tid = ctypes.c_long(tid)
    if not inspect.isclass(exctype):
        exctype = type(exctype)
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, ctypes.py_object(exctype))
    if res == 0:
        raise ValueError("invalid thread id")
    elif res != 1:
        # """if it returns a number greater than one, you're in trouble,
        # and you should call it again with exc=NULL to revert the effect"""
        ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
        raise SystemError("PyThreadState_SetAsyncExc failed")


def stop_thread(thread):
    _async_raise(thread.ident, SystemExit)


def main():
    setting.init()
    # grab the indexes of the facial landmarks

    print("[INFO] starting video stream thread...")
    setting.vs = VideoStream(src=1).start()
    time.sleep(1.0)

    facedetection_t = threading.Thread(target=facedetection_background, name='Face')
    facedetection_t.start()
    time.sleep(1.0)

    MainUI.main_ui()

    # setting.vs.stop()
    # stop_thread(facedetection_t)
    print("[INFO] stop video thread...")
    print("[INFO] Exit")
    sys.exit(1)


if __name__ == '__main__':  # 在win系统下必须要满足这个if条件
    main()
