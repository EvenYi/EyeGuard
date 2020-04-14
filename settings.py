import tkinter as tk
from PIL import ImageTk, Image

# Home page 左半边

root = tk.Tk()
root.title("Eye guard")
root.geometry('640x400')

left_canvas = tk.Canvas(root, width=154, height=404)
left_canvas.place(x=-2,y=-2)

photo = Image.open("left.jpg")
photo = photo.resize((154, 404), Image.ANTIALIAS)
left_bg = ImageTk.PhotoImage(photo)

left_canvas.create_image(0, 0, image=left_bg, anchor='nw')


toolBar_frame = tk.Frame(left_canvas,width = 150, height=120)
toolBar_frame.place(x=0,y=162)

home_button = tk.Button(toolBar_frame, text='Home page', bg='#2C3D55', width = 13, anchor='c',font=14, fg='#0A8E8B')
home_button.place(x=0,y=0)

setting_button = tk.Button(toolBar_frame, text='Setting', bg='#01FAE7', width = 13, anchor='c',font=14)
setting_button.place(x=0,y=40)


history_button = tk.Button(toolBar_frame, text='History', bg='#2C3D55', width = 13, anchor='c',font=14, fg='#0A8E8B')
history_button.place(x=0,y=80)

left_canvas.create_text(7,300, text='About us:\n\nsites.google.com/view/\neye-guard/homepage', anchor = 'nw', fill= '#01FAE7')
# home page右半边
right_frame = tk.Frame(root, bg = '#2C3D55', width = 490, height = 400)
right_frame.place(x=150, y=0)

mode_check_button = tk.Checkbutton(right_frame, text = 'Alert mode', bg = '#2C3D55', fg='#01FAE7', activebackground = '#2C3D55', font = 20)
mode_check_button.place(x=13,y=40)

mode_list = ['TBD1', 'TBD2', 'TBD3']

for i in range(len(mode_list)):
    radio_button = tk.Radiobutton(right_frame, text=mode_list[i], bg='#2C3D55', fg='#01FAE7', activebackground='#2C3D55',font=20)
    radio_button.place(x=20 + i*150,y=130)

music_check_button = tk.Checkbutton(right_frame, text = 'Music mode', bg = '#2C3D55', fg='#01FAE7', activebackground = '#2C3D55', font = 20)
music_check_button.place(x=13,y=200)


music_list = ['Pop music', 'Natural', 'Classic']

for i in range(len(music_list)):
    radio_button = tk.Radiobutton(right_frame, text=music_list[i], bg='#2C3D55', fg='#01FAE7', activebackground='#2C3D55',font=20)
    radio_button.place(x=20 + i*150,y=260)

apply_button = tk.Button(right_frame, width = 10, height = 2, bg = '#01FAE7', text = 'Apply', font = 20)
apply_button.place(x=350,y=323)



root.mainloop()