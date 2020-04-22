import tkinter as tk
import imutils
from PIL import ImageTk, Image
import cv2
import setting
import configparser


def home_page_show(root):
    right_frame = tk.Frame(root, bg='#2C3D55', width=490, height=400)
    right_frame.place(x=150, y=0)

    camera = tk.Frame(right_frame, width=323, height=292, bg='#2C3D55')
    camera.place(x=10, y=45)

    # Graphics window
    imageFrame = tk.Frame(camera, width=600, height=500)
    imageFrame.grid(row=0, column=0, padx=10, pady=2)

    # Capture video frames
    lmain = tk.Label(imageFrame)
    lmain.grid(row=0, column=0)

    def show_frame():
        frame = setting.vs.read()
        frame = imutils.resize(frame, width=310, height=292, )
        frame = cv2.flip(frame, 1)
        cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
        img = Image.fromarray(cv2image)
        imgtk = ImageTk.PhotoImage(image=img)
        lmain.imgtk = imgtk
        lmain.configure(image=imgtk)
        lmain.after(10, show_frame)

    # Slider window (slider controls stage position)

    show_frame()  # Display 2

    mode = tk.StringVar()
    mode.set(0)


    radio_button1 = tk.Radiobutton(right_frame, text='Adult', bg='#2C3D55', fg='#01FAE7', activebackground='#2C3D55',
                                   var=mode, value=0, font=20)
    radio_button2 = tk.Radiobutton(right_frame, text='Teenager', bg='#2C3D55', fg='#01FAE7', activebackground='#2C3D55',
                                   var=mode, value=1, font=20)
    radio_button1.place(x=34, y=320)
    radio_button2.place(x=200, y=320)

    label_status = tk.Label(right_frame, height=1, width=20, text='Current status', fg='#01FAE7', bg='#2C3D55', font=14,
                            anchor='w')
    label_status.place(x=350, y=30)
    return right_frame


def setting_page_show(root):
    right_frame = tk.Frame(root, bg='#2C3D55', width=490, height=400)
    right_frame.place(x=150, y=0)

    pop_var = tk.IntVar()
    pop_var.set(setting.IF_POP)
    mode_check_button = tk.Checkbutton(right_frame, text='Alert mode', bg='#2C3D55', fg='#01FAE7',
                                       activebackground='#2C3D55', font=20, var=pop_var)
    mode_check_button.place(x=13, y=40)

    music_var = tk.IntVar()
    music_var.set(setting.IF_MUSIC)
    music_check_button = tk.Checkbutton(right_frame, text='Music mode', bg='#2C3D55', fg='#01FAE7',
                                        activebackground='#2C3D55', font=20, var=music_var)
    music_check_button.place(x=13, y=150)

    music_list = ['Pop music', 'Natural', 'Classic']

    type = tk.StringVar()
    type.set(setting.MUSIC_TYPE)
    for i in range(len(music_list)):
        radio_button = tk.Radiobutton(right_frame, text=music_list[i], bg='#2C3D55', fg='#01FAE7',
                                      activebackground='#2C3D55', font=20, variable=type, value=music_list[i])
        radio_button.place(x=35 + i * 150, y=240)

    def apply():
        cf = configparser.ConfigParser()
        cf.read('./config.ini', encoding='utf-8')

        cf.set('Remind-Mode','IF_POP',str(pop_var.get()))
        cf.set('Remind-Mode', 'IF_MUSIC', str(music_var.get()))
        cf.set('Remind-Mode', 'MUSIC_TYPE', type.get())
        cf.write(open('./config.ini', 'r+', encoding='utf-8'))

        setting.IF_POP = pop_var.get()
        setting.IF_MUSIC = music_var.get()
        setting.MUSIC_TYPE = type.get()



    apply_button = tk.Button(right_frame, width=10, height=2, bg='#01FAE7', text='Apply', font=20, command=apply)
    apply_button.place(x=350, y=323)
    return right_frame


def history_page_show(root):
    right_frame = tk.Frame(root, bg='#2C3D55', width=490, height=400)
    right_frame.place(x=150, y=0)
    return right_frame