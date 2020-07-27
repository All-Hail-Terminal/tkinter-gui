from tkinter import *
from tkinter import colorchooser
from pygame import mixer

win = Tk()
win['background'] = '#283747'
mixer.init()
music = mixer.music.load('Ransom.mp3')

musiccount = 0
onetimeuse = 0
mixer.init()


def music_player():
    global musiccount
    global onetimeuse
    if onetimeuse == 0:
        mixer.music.play(-1)
        onetimeuse = 1
        musiccount = 1
    else:
        if musiccount == 0:
            mixer.music.unpause()
            musiccount = musiccount + 1
        else:
            mixer.music.pause()
            musiccount = 0


def start_click():
    b_start.destroy()
    b_settings.destroy()
    b_quit.destroy()

    def buttons_click():
        b_button_1 = Button(win, text='Button 1')
        b_button_1.place(x=150, y=200)

        b_button_2 = Button(win, text='Button 2')
        b_button_2.place(x=150, y=250)

        b_button_3 = Button(win, text='Button 3')
        b_button_3.place(x=150, y=300)

    def labels_click():
        b_label_1 = Button(win, text='Label 1')
        b_label_1.place(x=150, y=300)

        b_label_2 = Button(win, text='Label 2')
        b_label_2.place(x=150, y=350)
        
        b_label_3 = Button(win, text='Label 3')
        b_label_3.place(x=150, y=400)

    def quit_project_click():
        win.destroy()

    # MAIN GUI BUTTONS
    b_new_project = Button(win, text='New Project')
    b_new_project.place(x=50, y=50)

    b_buttons = Button(win, text='Buttons', command=buttons_click)
    b_buttons.place(x=50, y=150)

    b_labels = Button(win, text='Labels',command=labels_click)
    b_labels.place(x=50, y=250)

    b_quit_project = Button(win, text='Quit', command=quit_project_click, width=10)
    b_quit_project.place(x=700, y=550)


def settings_click():
    b_start.destroy()
    b_settings.destroy()
    b_quit.destroy()

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
        lb_height.destroy()
        lb_width.destroy()
        lb_click_here.destroy()
        color_chooser = colorchooser.askcolor(title='select color')
        win.configure(background=color_chooser[1])

    def music_click():
        b_save_settings.destroy()
        lb_color.destroy()
        height_slider.destroy()
        width_slider.destroy()
        b_save_settings.destroy()
        b_click_here.destroy()
        lb_height.destroy()
        lb_width.destroy()
        lb_click_here.destroy()

        def music_save_settings_click():
            volume_value = int(music_volume.get())
            volume_value = volume_value / 100
            mixer.music.set_volume(volume_value)

        # MUSIC BUTTONS
        b_music_save_settings = Button(win, text='Save Settings', command=music_save_settings_click)
        b_music_save_settings.place(x=250, y=250)

        # MUSIC LABELS
        lb_music = Label(win, text="Music: ")
        lb_music.place(x=260, y=100)

        lb_volume = Label(win, text='Music Volume')
        lb_volume.place(x=250, y=150)

        # MUSIC SLIDERS
        music_volume = Scale(win, from_=0, to=100, orient=HORIZONTAL)
        music_volume.place(x=350, y=135)

        # SETTINGS CHECKBOX
        cb_music = Checkbutton(win, text='ON', command=music_player)
        cb_music.place(x=350, y=100)

    # SETTINGS BUTTONS
    b_save_settings = Button(win, text='Save Settings', command=save_settings_click)
    b_save_settings.place(x=310, y=300)

    b_click_here = Button(win, text='Click Here', command=click_here_click)
    b_click_here.place(x=300, y=450)

    b_change_background_color = Button(win, text='Change Background Color', command=change_background_color_click)
    b_change_background_color.place(x=250, y=50)

    b_music = Button(win, text='Music', command=music_click)
    b_music.place(x=100, y=50)

    b_back = Button(win, text='Back')
    b_back.place(x=500, y=500)

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
