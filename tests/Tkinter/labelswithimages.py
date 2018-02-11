#!/bin/python3.5

import tkinter as tk
import os, sys

script_path = __file__
script_dir = os.path.dirname(__file__)
icon_path = os.path.join(script_dir, 'images', 'python_200x200.png')

explanation = """At present, only GIF and PPM/PGM
formats are supported, but an interface
exists to allow additional image file
formats to be added easily."""

root = tk.Tk()
icon = tk.PhotoImage(file=icon_path) # root precisa estar antes de photoimage ser usado

label = tk.Label(root, image=icon).pack(side=tk.RIGHT)
label2 = tk.Label(root, text=explanation, padx=10, justify=tk.LEFT).pack(side=tk.LEFT)

root.mainloop()

#c:\xampp\htdocs\python\tests\Tkinter\images\python_200x200.gif
#C:\xampp\htdocs\python\tests\Tkinter\images\python_200x200.gif
