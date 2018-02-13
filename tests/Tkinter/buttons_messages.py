#!/bin/python3

import tkinter as tk

def write_slogan():
    print('Tkinter is easy to use.')

def show_message(parent):
    frame = tk.Toplevel(parent)

    msg = tk.Message(frame, text='Message opened by button.')
    msg.pack()


root = tk.Tk()

frame = tk.Frame(root)
frame.pack()

button1 = tk.Button(frame, text='Quit', command=quit, fg='red')
button1.pack(side=tk.LEFT)

button2 = tk.Button(frame, text='Hello', command=lambda: show_message(root))
button2.pack(side=tk.LEFT)

root.mainloop()
