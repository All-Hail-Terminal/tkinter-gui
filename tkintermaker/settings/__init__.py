import tkinter
from tkinter import colorchooser


def main(win):
    """Do settings things."""
    def save_settings_click():
        height_value = str(height_slider.get())
        width_value = str(width_slider.get())
        total = height_value + 'x' + width_value
        win.geometry(total)

    def click_here_click():
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
        height_entry = tkinter.Entry(win)
        height_entry.place(x=210, y=150)

        width_entry = tkinter.Entry(win)
        width_entry.place(x=350, y=150)

        # CLICK HERE BUTTONS
        b_click_here_save_settings = tkinter.Button(win, text='Save Settings', command=click_here_save_settings_click)
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
    b_save_settings = tkinter.Button(win, text='Save Settings', command=save_settings_click)
    b_save_settings.place(x=310, y=300)

    b_click_here = tkinter.Button(win, text='Click Here', command=click_here_click)
    b_click_here.place(x=300, y=450)

    b_change_background_color = tkinter.Button(win, text='Change Background Color', command=change_background_color_click)
    b_change_background_color.place(x=600, y=150)

    # SETTINGS LABELS
    lb_height = tkinter.Label(win, text='HEIGHT')
    lb_height.place(x=260, y=120)

    lb_width = tkinter.Label(win, text='WIDTH')
    lb_width.place(x=380, y=120)

    lb_color = tkinter.Label(win, text="BACKGROUND COLOR")
    lb_color.place(x=285, y=200)

    lb_click_here = tkinter.Label(win, text="Or insert the window's dimensions, by clicking in the button below")
    lb_click_here.place(x=300, y=400)

    # SLIDERS
    height_slider = tkinter.Scale(win, from_=800, to=1920, orient=tkinter.HORIZONTAL)
    height_slider.place(x=230, y=150)

    width_slider = tkinter.Scale(win, from_=600, to=1080, orient=tkinter.HORIZONTAL)
    width_slider.place(x=350, y=150)
