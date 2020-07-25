from tkinter import *


win = Tk()

img = PhotoImage(file="background.png")
Label(win, image=img, bg="grey").pack()
win.wm_attributes('-transparentcolor', 'grey')


def start_click():
    start = start_click
    if start == start_click:
        b_start.destroy()


# General GUI
b_start = Button(win, text='Start', command=start_click)
b_start.place(x=390, y=250)

win.geometry('800x600')
win.mainloop()
