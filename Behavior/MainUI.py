import sys

sys.path.append(r'..\Algorithm')
sys.path.append(r'..\OperatingSystem')

import tkinter as tk
from PIL import ImageTk, Image
from audio import playaudio
import Pages
import setting
import inspect
import ctypes
import threading
import time
import tkinter.messagebox



def star_eyeguard(button):
    print("[INFO]: Start eyeguard.")
    button.config(text='Stop', command=lambda : stop_eyeguard(button))
    if setting.STATUS_EB == -1:
        setting.STATUS_EB = threading.Thread(target=eyeFatigue_judgment, name='EyeBlinks')
        setting.STATUS_EB.start()
    if setting.STATUS_HP == -1:
        setting.STATUS_HP = threading.Thread(target=head_posture_judgment, name='HeadPosture')
        setting.STATUS_HP.start()

def stop_eyeguard(button):
    button.config(text = 'Start', command=lambda :star_eyeguard(button))
    

def eyeFatigue_judgment():
    while True:
        if setting.STATUS_EB_END != True:
            point_1 = setting.TOTAL
            time.sleep(32.0)
            point_2 = setting.TOTAL
            print("[INFO]: Current eye blinks: " + str(point_2 - point_1))
            if (point_2 - point_1) < 10:
                print("[INFO] Your eyes is fatigue")
                if setting.IF_POP == '1':
                    tkinter.messagebox.showinfo('Eyeguard', 'You are tired. Go have some rests!')
                if setting.IF_MUSIC == '1':
                    playaudio()

        else:
            break


def head_posture_judgment():
    while True:
        if setting.STATUS_HP_END != True:
            time.sleep(60.0)
            tkinter.messagebox.showinfo('Eyeguard', 'You are close. Go have some rests!')
            print("[INFO] Head posture: " + setting.HP_CODE)
        else:
            break


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


def main_ui():
    # Home page 左半边

    root = tk.Tk()
    root.resizable(0, 0)
    root.title("Eye guard")
    root.geometry('640x400')

    # 左边的背景放在画布中
    left_canvas = tk.Canvas(root, width=154, height=404)
    left_canvas.place(x=-2, y=-2)

    # 载入图片
    photo = Image.open("Behavior/Images/left.jpg")
    photo = photo.resize((154, 404), Image.ANTIALIAS)
    left_bg = ImageTk.PhotoImage(photo)
    left_canvas.create_image(0, 0, image=left_bg, anchor='nw')

    # 左边按钮栏
    toolBar_frame = tk.Frame(left_canvas, width=150, height=120)
    toolBar_frame.place(x=0, y=162)

    # 加载三个页面
    frame_home = Pages.home_page_show(root)
    frame_setting = Pages.setting_page_show(root)
    frame_history = Pages.history_page_show(root)

    v = tk.StringVar()
    status_label = tk.Label(frame_home, height=15, width=18, bg='white', anchor='nw', textvariable=v)
    status_label.place(x=350, y=45)

    def updating():
        while True:
            v.set("Total Eye Blins: \n " + str(setting.TOTAL) + " \n " + "Head Posture: \n" + str(setting.HP_CODE))
            if setting.END:
                break

    if setting.STATUS_T == -1:
        setting.STATUS_T = threading.Thread(target=updating, name='Status')
        setting.STATUS_T.start()


    start_button = tk.Button(frame_home, width=10, height=2, bg='#01FAE7', text='Start', font=20, command=lambda :star_eyeguard(start_button))
    start_button.place(x=350, y=323)


    # 调选中或未选中整颜色的方法
    def button_setting(button, other_button):
        button.config(fg='black', bg='#01FAE7')
        for each in other_button:
            each.config(fg='#0A8E8B', bg='#2C3D55')

    # 显示当前选中页面
    def show_page(button, other_button):
        if button['text'] == 'Home page':
            frame_home.lift()
        elif button['text'] == 'Setting':
            frame_setting.lift()
        else:
            frame_history.lift()

        button_setting(button, other_button)

    # 声明按钮们
    home_button = tk.Button(toolBar_frame, text='Home page', bg='#01FAE7', width=13, anchor='c', font=14, )
    home_button.place(x=0, y=0)

    setting_button = tk.Button(toolBar_frame, text='Setting', bg='#2C3D55', width=13, anchor='c', font=14, fg='#0A8E8B')
    setting_button.place(x=0, y=40)

    history_button = tk.Button(toolBar_frame, text='History', bg='#2C3D55', width=13, anchor='c', font=14, fg='#0A8E8B')
    history_button.place(x=0, y=80)

    # 将方法塞进按钮
    home_button.config(command=lambda: show_page(home_button,
                                                 [setting_button, history_button]))
    setting_button.config(command=lambda: show_page(setting_button,
                                                    [home_button, history_button]))
    history_button.config(command=lambda: show_page(history_button,
                                                    [home_button, setting_button]))

    # about us
    left_canvas.create_text(7, 300, text='About us:\n\nsites.google.com/view/\neye-guard/homepage', anchor='nw',
                            fill='#01FAE7')
    frame_home.lift()
    frame_home.update()

    def close_app():
        setting.STATUS_EB_END = True
        setting.STATUS_HP_END = True
        stop_thread(setting.STATUS_T)
        time.sleep(2.0)
        setting.END = True
        print("[INFO] stop status thread...")
        root.destroy()

    root.protocol('WM_DELETE_WINDOW', close_app)
    root.mainloop()
