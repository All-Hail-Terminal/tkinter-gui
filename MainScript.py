from tkinter import *

win = Tk()

img = PhotoImage(file="background.png")
Label(win, image=img, bg="grey").pack()
win.wm_attributes('-transparentcolor', 'grey')


def start_click():
    start = start_click
    if start == start_click:
        b_start.destroy()
        b_settings.destroy()
        b_quit.destroy()

        def buttons_click():
            b_button_1 = Button(win, text='Button 1')
            b_button_1.place(x=150, y=200)

        # Buttons GUI
        b_buttons = Button(win, text='Buttons', command=buttons_click)
        b_buttons.place(x=150, y=150)


def settings_click():
    settings = settings_click
    if settings == settings_click:
        b_start.destroy()
        b_settings.destroy()
        b_quit.destroy()

        def save_settings_click():
            save_settings = save_settings_click
            if save_settings == save_settings_click:
                height_value = str(height_slider.get())
                width_value = str(width_slider.get())
                total = height_value + 'x' + width_value
                win.geometry(total)


        # SETTINGS BUTTONS
        b_save_settings = Button(win, text='Save Settings', command=save_settings_click)
        b_save_settings.place(x=310, y=250)

        # SETTINGS LABELS
        lb_height = Label(win, text='HEIGHT')
        lb_height.place(x=260, y=120)

        lb_width = Label(win, text='WIDTH')
        lb_width.place(x=380, y=120)

        # SLIDERS
        height_slider = Scale(win, from_=800, to=1920, orient=HORIZONTAL)
        height_slider.place(x=230, y=150)

        width_slider = Scale(win, from_=600, to=1080, orient=HORIZONTAL)
        width_slider.place(x=350, y=150)


# General GUI
b_start = Button(win, text='Start', command=start_click, width=10)
b_start.place(x=350, y=250)

b_settings = Button(win, text='Settings', command=settings_click, width=10)
b_settings.place(x=350, y=300)

b_quit = Button(win, text='Quit', width=10)
b_quit.place(x=350, y=350)

win.geometry('800x600')
win.mainloop()
