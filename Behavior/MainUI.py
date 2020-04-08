import tkinter as tk


def quick_start():
    print('quick start')
def customized():
    print('customized')


window_width = 640
window_height = 400
times = 0.25


window = tk.Tk()
window.title("Eye guard")
window.geometry(''+str(window_width)+'x'+str(window_height))



frm_up = tk.Frame(window, width=window_width, height = window_height * times, bg='red')
frm_down = tk.Frame(window, width=window_width, height=window_height * (1-times),bg='green')
frm_down_right = tk.Frame(frm_down, width= window_width * 0.3, height=window_height * (1-times), bg='yellow')

frm_up.pack()
frm_down.pack()
frm_down_right.place(x=0.7*window_width, y=0)

button_quick = tk.Button(frm_down_right, text = 'Quick start', width = 20, command = quick_start)
button_quick.place(x = window_width * 0.3 * 0.12, y = 0.15 * window_height * (1-times))

button_customized = tk.Button(frm_down_right, text = 'Customized mode', width = 20, command = quick_start)
button_customized.place(x = window_width * 0.3 * 0.12, y = 0.45 * window_height * (1-times))

button_tbd1 = tk.Button(frm_down_right, text = 'tbd1', width = 20, command = quick_start)
button_tbd1.place(x = window_width * 0.3 * 0.12, y = 0.75 * window_height * (1-times))
# frm_down_rim_up
button_personal_data = tk.Button(frm_up, text = 'Personal data', width=20)
button_TBD = tk.Button(frm_up, text = 'tbd1', width=20)
button_TBD2 = tk.Button(frm_up, text = 'tbd2', width=20)


button_personal_data.place(x = window_width * 0.04, y = window_height * times * 0.3)
button_TBD.place(x = window_width * 0.38, y = window_height * times * 0.3)
button_TBD2.place(x = window_width * 0.72, y = window_height * times * 0.3)
window.mainloop()