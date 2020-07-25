import tkinter


def main(win):
    """Do main things."""
    def buttons_click():
        b_button_1 = tkinter.Button(win, text='Button 1')
        b_button_1.place(x=150, y=200)

    # Buttons GUI
    b_buttons = tkinter.Button(win, text='Buttons', command=buttons_click)
    b_buttons.place(x=150, y=150)
