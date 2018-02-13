#!/bin/python3

import tkinter as tk

def main():
    whatever_you_do = "Whatever you do will be insignificant, but it is very important that you do it.\n(Mahatma Gandhi)"

    root = tk.Tk()

    msg = tk.Message(root, text=whatever_you_do)
    msg.config(bg='lightgreen', font=('times', 24, 'italic'))
    msg.pack()

    root.mainloop()


if __name__ == '__main__':
    main()
