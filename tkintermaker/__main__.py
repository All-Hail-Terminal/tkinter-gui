"""MIT License.

Copyright (c) 2020 All-Hail-Terminal

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import typing

import tkinter

import main
import settings

win = tkinter.Tk()

tkinter.Label(win, bg="grey").pack()
win.wm_attributes('-transparentcolor', 'grey')


def button_caller(func: typing.Callable):
    """Call a button's function."""
    def predictate():
        b_start.destroy()
        b_settings.destroy()
        b_quit.destroy()
        func(win)
    return predictate


# General GUI
b_start = tkinter.Button(
    win,
    text='Start',
    command=button_caller(main.main),
    width=10,
)
b_start.place(x=350, y=250)

b_settings = tkinter.Button(
    win,
    text='Settings',
    command=button_caller(settings.main),
    width=10,
)
b_settings.place(x=350, y=300)

b_quit = tkinter.Button(win, text='Quit', width=10)
b_quit.place(x=350, y=350)

win.geometry('800x600')
win.mainloop()
