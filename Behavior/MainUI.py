import sys
sys.path.append(r'C:\Users\yangy\University of Rochester\CSC412 HCI\FinalProject\EyeGuard\Algorithm')
import tkinter as tk
from PIL import ImageTk, Image
import Pages
import setting
import cv2
import imutils


def main_ui():
    # Home page 左半边

    root = tk.Tk()
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
    frame_home.lift()

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
    home_button = tk.Button(toolBar_frame, text='Home page', bg='#01FAE7', width=13, anchor='c', font=14)
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
    root.mainloop()
