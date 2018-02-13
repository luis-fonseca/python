#!/bin/python3

import tkinter as tk

def write_slogan():
    print('Tkinter is easy to use.')

root = tk.Tk()

frame = tk.Frame(root)
frame.pack()

button1 = tk.Button(frame, text='Quit', command=quit, fg='red')
button1.pack(side=tk.LEFT)

button2 = tk.Button(frame, text='Hello', command=write_slogan)
button2.pack(side=tk.LEFT)

root.mainloop()
