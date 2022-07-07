import tkinter as tk
import buttons as bt
from tkinter import *
from tkinter import ttk
import variables



variables.moves_done = []
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
root.iconbitmap(variables.resource_path("rubix.ico"))
canvas = tk.Canvas(root, width = 500, height=240)
canvas.pack()


labelTitle = tk.Label(root, text= "Welcome to the Rubix Reverser", font=("Yu Gothic", 25))    # Courier Century Gothic
labelSubtitle = tk.Label(root, text= "Enter your moves (B for buttons)", font=("Franklin Gothic Book", 15, "bold"))
canvas.create_rectangle(450, 120.5, 60, 118.5, fill='black')

def comboadd(event):

    variables.moves_done.append(myCombo.get())
    label = Label(root, text ="                        added                          ")
    canvas.create_window(250, 220, window=label)

def reverse():
    if len(variables.moves_done) > 0:
        variables.moves_done.reverse()

        for x in range(len(variables.moves_done)):
            if len(variables.moves_done[x]) == 1:
                reversed_move = variables.moves_done[x] + "'"
                variables.moves_done[x] = reversed_move
            elif "'" in variables.moves_done[x]:
                variables.moves_done[x] = variables.moves_done[x][:-1]           
                
        moves = ' '.join(variables.moves_done)
         
        label = Label(root, text ="               Reversed: " + str(moves) + "                ")
        canvas.create_window(250, 220, window=label)                                  
        variables.moves_done = []
    else:  
        label = Label(root, text ="                           No moves to reverse                           ")
        canvas.create_window(250, 220, window=label)                                  

def remove_move():
    try:
        variables.moves_done.pop() 
        label = Label(root, text ="                     Removed last move                     ")
        canvas.create_window(250, 220, window=label)
    except:
        label = Label(root, text ="                     no moves to remove                     ")
        canvas.create_window(250, 220, window=label)
myCombo = ttk.Combobox(root, value= moves_available)
myCombo.current(0)
myCombo.bind("<<ComboboxSelected>>", comboadd)
canvas.create_window(250, 150, window = myCombo)
myButtonReverse = Button(root, text = "Reverse", command = reverse) 
canvas.create_window(200, 190, window= myButtonReverse)
myButtonRemove = Button(root, text="Remove mode", command = remove_move)
canvas.create_window(290, 190, window= myButtonRemove)

canvas.create_window(250, 50, window=labelTitle)
canvas.create_window(250, 100, window=labelSubtitle)


root.bind("<b>", bt.buttonBox)
root.bind("<B>", bt.buttonBox)
root.resizable(False, False) # stop window from being resized
root.mainloop()  
