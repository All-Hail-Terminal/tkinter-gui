from tkinter import *
from tkinter import colorchooser

win = Tk()

Label(win, bg="grey").pack()
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
    global COLORS
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

        def click_here_click():
            click_here = click_here_click
            if click_here == click_here_click:
                b_save_settings.destroy()
                lb_color.destroy()
                height_slider.destroy()
                width_slider.destroy()
                b_save_settings.destroy()

                def click_here_save_settings_click():
                    click_here_save_settings = click_here_save_settings_click
                    if click_here_save_settings == click_here_save_settings_click:
                        height_entry_get = str(height_entry.get())
                        width_entry_get = str(width_entry.get())
                        win_geometry = height_entry_get + 'x' + width_entry_get
                        win.geometry(win_geometry)

                # CLICK HERE ENTRIES
                height_entry = Entry(win)
                height_entry.place(x=210, y=150)

                width_entry = Entry(win)
                width_entry.place(x=350, y=150)

                # CLICK HERE BUTTONS
                b_click_here_save_settings = Button(win, text='Save Settings', command=click_here_save_settings_click)
                b_click_here_save_settings.place(x=310, y=250)

        def change_background_color_click():
            b_save_settings.destroy()
            lb_color.destroy()
            height_slider.destroy()
            width_slider.destroy()
            b_save_settings.destroy()
            b_click_here.destroy()
            change_background_color = change_background_color_click
            if change_background_color == change_background_color_click:
                color_chooser = colorchooser.askcolor(title='select color')
                win.configure(background=color_chooser[1])

        # SETTINGS BUTTONS
        b_save_settings = Button(win, text='Save Settings', command=save_settings_click)
        b_save_settings.place(x=310, y=300)

        b_click_here = Button(win, text='Click Here', command=click_here_click)
        b_click_here.place(x=300, y=450)

        b_change_background_color = Button(win, text='Change Background Color', command=change_background_color_click)
        b_change_background_color.place(x=600, y=150)

        # SETTINGS LABELS
        lb_height = Label(win, text='HEIGHT')
        lb_height.place(x=260, y=120)

        lb_width = Label(win, text='WIDTH')
        lb_width.place(x=380, y=120)

        lb_color = Label(win, text="BACKGROUND COLOR")
        lb_color.place(x=285, y=200)

        lb_click_here = Label(win, text="Or insert the window's dimensions, by clicking in the button below")
        lb_click_here.place(x=300, y=400)

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
