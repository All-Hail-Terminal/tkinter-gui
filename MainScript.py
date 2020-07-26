from tkinter import *
from tkinter import colorchooser
import tkinter.font as tkFont

root = Tk()
menu = Frame(root)
menu.grid(padx=20, pady=20)
start = Frame(root)
settings = Frame(root)

# CONFIG

fontStyle = tkFont.Font(family="Lucida Grande", size=20)
small_font = tkFont.Font(family="Lucida Grande", size=15)

# MENU FUNCTIONS


def open_settings():
    menu.grid_forget()
    settings.grid()


def open_start():
    menu.grid_forget()
    start.grid()


def quit_prg():
    exit()


# SETTINGS FUNCTIONS


def save_settings():
    height_value = str(height_slider.get())
    width_value = str(width_slider.get())
    total = height_value + 'x' + width_value
    root.geometry(total)


def choose_color():
    color_chooser = colorchooser.askcolor(title='select color')
    root.configure(background=color_chooser[1])


# BACK COMMANDS


def startback():
    start.grid_forget()
    menu.grid()


def settingsback():
    settings.grid_forget()
    menu.grid()


# START BUTTONS

b_start = Button(menu, text="Start", command=open_start, font=fontStyle)
b_start.grid(row=0, column=0)

b_test = Button(start, text="test", font=fontStyle)
b_test.grid(row=1, column=0)

start_back = Button(start, text="Back", command=startback, font=fontStyle)
start_back.grid(row=1, column=2)

# SETTINGS BUTTONS

b_settings = Button(menu, text="Settings", command=open_settings, font=fontStyle)
b_settings.grid(row=0, column=1)

l_height = Label(settings, text="HEIGHT", font=small_font)
l_height.grid(row=0, column=0)

height_slider = Scale(settings, from_=800, to=1920, orient=HORIZONTAL)
height_slider.grid(row=1, column=0)

l_width = Label(settings, text="WIDTH", font=small_font)
l_width.grid(row=0, column=1)

width_slider = Scale(settings, from_=600, to=1080, orient=HORIZONTAL)
width_slider.grid(row=1, column=1)

b_save = Button(settings, text="Save", command=save_settings, font=fontStyle)
b_save.grid(row=2, column=0)

b_choose_color = Button(settings, text="Choose Background Color", command=choose_color, font=fontStyle)
b_choose_color.grid(row=3, column=0)

settings_back = Button(settings, text="Back", command=settingsback, font=fontStyle)
settings_back.grid(row=1, column=2)

# QUIT BUTTON

b_quit = Button(menu, text="Quit", command=quit_prg, font=fontStyle)
b_quit.grid(row=1, column=0, padx=50, pady=50)

# END

root.geometry('800x600')
root.mainloop()
