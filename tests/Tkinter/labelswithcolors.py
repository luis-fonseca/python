#!/bin/python3.5

import tkinter as tk

counter = 0
def count_label(label):

    def count():
        global counter

        label.after(1000, count)
        counter += 1
        label.config(text=str(counter))

    # deve ser chamado dessa forma ou ocorrerá erro por conta do limite da recursividade
    count()


root = tk.Tk()
root.title('Counting values ...')

label = tk.Label(root, fg='green')
label.pack() # se usar no fim da primeira linha retornará none e impedirá de usar .config na função
count_label(label)

button1 = tk.Button(root, text='Stop timer', width=25, command=root.destroy).pack()

root.mainloop()
