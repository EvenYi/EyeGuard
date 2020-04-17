import sys
sys.path.append(r'C:\Users\yangy\University of Rochester\CSC412 HCI\FinalProject\EyeGuard\Algorithm')
sys.path.append(r'C:\Users\yangy\University of Rochester\CSC412 HCI\FinalProject\EyeGuard\Behavior')
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

if __name__ == '__main__':  # 在win系统下必须要满足这个if条件
    setting.init()
    # grab the indexes of the facial landmarks

    print("[INFO] starting video stream thread...")
    setting.vs=VideoStream(src=1).start()
    time.sleep(1.0)

    facedetection_t = threading.Thread(target=facedetection_background)
    facedetection_t.start()
    time.sleep(3)
    MainUI.main_ui()
    _FINISH = True
    facedetection_t.join()
    setting.STATUS_T.join()

    # stop_thread(setting.STATUS_T)
    # print("[INFO] stop status thread...")
    # stop_thread(facedetection_t)
    # print("[INFO] stop video thread...")
    #
    # sys.exit(-1)
    # print("[INFO] Exit")



