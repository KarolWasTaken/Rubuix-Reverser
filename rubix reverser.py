import tkinter as tk
from tkinter import *
from tkinter import ttk
import sys, os


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try: 
        # PyInstaller creates a temp folder and stores path in _MEIPASS             # thanks stackoverflow :)
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

global moves_done
moves_done = []
moves_available = [
    "U",
    "D",
    "R",
    "L",
    "F",
    "B",
    "U'",
    "D'",
    "R'",
    "L'",
    "F'",
    "B'",
    "U2",
    "D2",
    "R2",
    "L2",
    "F2",
    "B2"
]

root = Tk()
root.title("Rubix Reverser")
root.iconbitmap(resource_path("rubix.ico"))
canvas = tk.Canvas(root, width = 500, height=240)
canvas.pack()

labelTitle = tk.Label(root, text= "Welcome to the Rubix Reverser", font=("Yu Gothic", 25))    # Courier Century Gothic
labelSubtitle = tk.Label(root, text= "Enter your moves", font=("Franklin Gothic Book", 15, "bold"))
canvas.create_rectangle(450, 120.5, 60, 118.5, fill='black')

def comboadd(event):
    global moves_done

    moves_done.append(myCombo.get())
    label = Label(root, text ="added")
    canvas.create_window(250, 220, window=label)

def reverse():
    global moves_done
    moves_done.reverse()
    moves = ' '.join(moves_done)
    
    label = Label(root, text ="Reversed: " + str(moves))
    canvas.create_window(250, 220, window=label)                                  
    moves_done = []



myCombo = ttk.Combobox(root, value= moves_available)
myCombo.current(0)
myCombo.bind("<<ComboboxSelected>>", comboadd)
canvas.create_window(250, 150, window = myCombo)
myButtonReverse = Button(root, text = "Reverse", command = reverse) 
canvas.create_window(250, 190, window= myButtonReverse)

canvas.create_window(250, 50, window=labelTitle)
canvas.create_window(250, 100, window=labelSubtitle)
root.resizable(False, False) # stop window from being resized
root.mainloop()  