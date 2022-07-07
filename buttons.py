import tkinter as tk
from tkinter import *
from tkinter import ttk
import variables


def setflag(event): # flag to make sure options menu is only opened once.
    variables.ontop = False 

def buttonBox(self):

    if not variables.ontop:
        root = tk.Toplevel()             # make sure options is only open once
        root.bind('<Destroy>', setflag)
    variables.ontop = True


    root.title("Rubix Reverser Buttons")
    root.iconbitmap(variables.resource_path("rubix.ico"))
    canvas = tk.Canvas(root, width = 500, height=240)
    canvas.pack()

    labelTitle = tk.Label(root, text= "Here are your buttons :)", font=("Yu Gothic", 25))    # Courier Century Gothic
    canvas.create_window(250, 50, window=labelTitle)
    

    """           THIS IS GOING TO LOOK PRETTY MESSY 
                  ALL OF THE BUTTONS WILL GO HERE                """


    def U():
        variables.moves_done.append("U")
    def D():
        variables.moves_done.append("D")
    def R():
        variables.moves_done.append("R")
    def L():
        variables.moves_done.append("L")
    def F():
        variables.moves_done.append("F")
    def B():
        variables.moves_done.append("B")

    def Up():
        variables.moves_done.append("U'")
    def Dp():
        variables.moves_done.append("D'")
    def Rp():
        variables.moves_done.append("R'")
    def Lp():
        variables.moves_done.append("L'")
    def Fp():
        variables.moves_done.append("F'")
    def Bp():
        variables.moves_done.append("B'")

    def U2():
        variables.moves_done.append("U2")
    def D2():
        variables.moves_done.append("D2")
    def R2():
        variables.moves_done.append("R2")
    def L2():
        variables.moves_done.append("L2")
    def F2():
        variables.moves_done.append("F2")
    def B2():
        variables.moves_done.append("B2")

    myButton1 = Button(root, text = "U", command = U, width = 4, height= 2) 
    canvas.create_window(130, 110, window= myButton1)
    myButton2 = Button(root, text = "D", command = D, width = 4, height= 2) 
    canvas.create_window(180, 110, window= myButton2)
    myButton3 = Button(root, text = "R", command = R, width = 4, height= 2) 
    canvas.create_window(230, 110, window= myButton3)
    myButton4 = Button(root, text = "L", command = L, width = 4, height= 2) 
    canvas.create_window(280, 110, window= myButton4)
    myButton5 = Button(root, text = "F", command = F, width = 4, height= 2) 
    canvas.create_window(330, 110, window= myButton5)
    myButton6 = Button(root, text = "B", command = B, width = 4, height= 2) 
    canvas.create_window(380, 110, window= myButton6)

    myButton7 = Button(root, text = "U'", command = Up, width = 4, height= 2) 
    canvas.create_window(130, 160, window= myButton7)
    myButton8 = Button(root, text = "D'", command = Dp, width = 4, height= 2) 
    canvas.create_window(180, 160, window= myButton8)
    myButton9 = Button(root, text = "R'", command = Rp, width = 4, height= 2) 
    canvas.create_window(230, 160, window= myButton9)
    myButton10 = Button(root, text = "L'", command = Lp, width = 4, height= 2) 
    canvas.create_window(280, 160, window= myButton10)
    myButton11 = Button(root, text = "F'", command = Fp, width = 4, height= 2) 
    canvas.create_window(330, 160, window= myButton11)
    myButton12 = Button(root, text = "B'", command = Bp, width = 4, height= 2) 
    canvas.create_window(380, 160, window= myButton12)

    myButton13 = Button(root, text = "U2", command = U2, width = 4, height= 2) 
    canvas.create_window(130, 210, window= myButton13) 
    myButton14 = Button(root, text = "D2", command = D2, width = 4, height= 2) 
    canvas.create_window(180, 210, window= myButton14)
    myButton15 = Button(root, text = "R2", command = R2, width = 4, height= 2) 
    canvas.create_window(230, 210, window= myButton15)
    myButton16 = Button(root, text = "L2", command = L2, width = 4, height= 2) 
    canvas.create_window(280, 210, window= myButton16)
    myButton17 = Button(root, text = "F2", command = F2, width = 4, height= 2) 
    canvas.create_window(330, 210, window= myButton17)
    myButton18 = Button(root, text = "B2", command = B2, width = 4, height= 2) 
    canvas.create_window(380, 210, window= myButton18)

    """           Wow. That is big.                             """

    root.resizable(False, False) # stop window from being resized
    root.mainloop()