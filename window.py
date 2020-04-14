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

home_button = tk.Button(toolBar_frame, text='Home page', bg='#01FAE7', width = 13, anchor='c',font=14)
home_button.place(x=0,y=0)

setting_button = tk.Button(toolBar_frame, text='Setting', bg='#2C3D55', width = 13, anchor='c',font=14, fg='#0A8E8B')
setting_button.place(x=0,y=40)


history_button = tk.Button(toolBar_frame, text='History', bg='#2C3D55', width = 13, anchor='c',font=14, fg='#0A8E8B')
history_button.place(x=0,y=80)

left_canvas.create_text(7,300, text='About us:\n\nsites.google.com/view/\neye-guard/homepage', anchor = 'nw', fill= '#01FAE7')

# home page右半边
right_frame = tk.Frame(root, bg = '#2C3D55', width = 490, height = 400)
right_frame.place(x=150, y=0)

camera = tk.Canvas(right_frame, width = 323, height = 292)
camera.place(x=10, y=10)

mode = 'Adult'

radio_button1 = tk.Radiobutton(right_frame, text = 'Adult', bg = '#2C3D55', fg = '#01FAE7', activebackground = '#2C3D55', variable = mode, value = 'Adult', font = 20)
radio_button2 = tk.Radiobutton(right_frame, text = 'Teenager', bg = '#2C3D55', fg='#01FAE7', activebackground = '#2C3D55',variable = mode, value = 'Teenager', font = 20)
radio_button1.place(x=34,y=335)
radio_button2.place(x=200, y=335)

label_status = tk.Label(right_frame, height = 1, width = 20, text = 'Current status', fg = '#01FAE7', bg = '#2C3D55', font = 14,anchor = 'w')
label_status.place(x=350, y=0)

status_label = tk.Label(right_frame, height = 15, width = 18, bg = 'blue', anchor = 'nw')
status_label.place(x=350,y=45)



start_button = tk.Button(right_frame, width = 10, height = 2, bg = '#01FAE7', text = 'Start', font = 20)
start_button.place(x=350,y=323)
root.mainloop()