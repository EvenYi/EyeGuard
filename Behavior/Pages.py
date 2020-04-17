import tkinter as tk
import imutils
from PIL import ImageTk, Image
import cv2
import setting

def home_page_show(root):
    right_frame = tk.Frame(root, bg='#2C3D55', width=490, height=400)
    right_frame.place(x=150, y=0)

    camera = tk.Frame(right_frame, width=323, height=292, bg = '#2C3D55')
    camera.place(x=10, y=45)


    # Graphics window
    imageFrame = tk.Frame(camera, width=600, height=500)
    imageFrame.grid(row=0, column=0, padx=10, pady=2)

    # Capture video frames
    lmain = tk.Label(imageFrame)
    lmain.grid(row=0, column=0)
    cap = setting.vs

    def show_frame():
        frame = cap.read()
        frame = imutils.resize(frame, width=310, height=292,)
        frame = cv2.flip(frame, 1)
        cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
        img = Image.fromarray(cv2image)
        imgtk = ImageTk.PhotoImage(image=img)
        lmain.imgtk = imgtk
        lmain.configure(image=imgtk)
        lmain.after(10, show_frame)

    # Slider window (slider controls stage position)

    show_frame()  # Display 2

    mode = 'Adult'

    radio_button1 = tk.Radiobutton(right_frame, text='Adult', bg='#2C3D55', fg='#01FAE7', activebackground='#2C3D55',
                                   variable=mode, value='Adult', font=20)
    radio_button2 = tk.Radiobutton(right_frame, text='Teenager', bg='#2C3D55', fg='#01FAE7', activebackground='#2C3D55',
                                   variable=mode, value='Teenager', font=20)
    radio_button1.place(x=34, y=335)
    radio_button2.place(x=200, y=335)

    label_status = tk.Label(right_frame, height=1, width=20, text='Current status', fg='#01FAE7', bg='#2C3D55', font=14,
                            anchor='w')
    label_status.place(x=350, y=0)

    status_label = tk.Label(right_frame, height=15, width=18, bg='blue', anchor='nw')
    status_label.place(x=350, y=45)

    start_button = tk.Button(right_frame, width=10, height=2, bg='#01FAE7', text='Start', font=20)
    start_button.place(x=350, y=323)

    return right_frame

def setting_page_show(root):
    right_frame = tk.Frame(root, bg='#2C3D55', width=490, height=400)
    right_frame.place(x=150, y=0)

    mode_check_button = tk.Checkbutton(right_frame, text='Alert mode', bg='#2C3D55', fg='#01FAE7',
                                       activebackground='#2C3D55', font=20)
    mode_check_button.place(x=13, y=40)

    mode_list = ['TBD1', 'TBD2', 'TBD3']

    for i in range(len(mode_list)):
        radio_button = tk.Radiobutton(right_frame, text=mode_list[i], bg='#2C3D55', fg='#01FAE7',
                                      activebackground='#2C3D55', font=20)
        radio_button.place(x=20 + i * 150, y=130)

    music_check_button = tk.Checkbutton(right_frame, text='Music mode', bg='#2C3D55', fg='#01FAE7',
                                        activebackground='#2C3D55', font=20)
    music_check_button.place(x=13, y=200)

    music_list = ['Pop music', 'Natural', 'Classic']

    for i in range(len(music_list)):
        radio_button = tk.Radiobutton(right_frame, text=music_list[i], bg='#2C3D55', fg='#01FAE7',
                                      activebackground='#2C3D55', font=20)
        radio_button.place(x=20 + i * 150, y=260)

    apply_button = tk.Button(right_frame, width=10, height=2, bg='#01FAE7', text='Apply', font=20)
    apply_button.place(x=350, y=323)
    return right_frame

def history_page_show(root):
    right_frame = tk.Frame(root, bg='#2C3D55', width=490, height=400)
    right_frame.place(x=150, y=0)
    return right_frame