from Tkinter import *
import tkFont
from tkMessageBox import *


root = Tk()

root.title('CEDBANGER')

top = Toplevel()
top.wm_withdraw()

def yahOrNah():
    if askyesno('CEDBANGER','Are you ready?'):
        theGame()


def theGame():
    #showinfo('CEDBANGER', "Let's make magic!")
    root.wm_withdraw()
    top.wm_deiconify()

    
def Quit():
    root.destroy()


mainCanvas = Canvas(root, width = 500, height = 480, bg = "blue")
photo = PhotoImage(file = 'lightning1.gif')
mainCanvas.create_image(200,240, image=photo)
mainCanvas.pack()


topCanvas = Canvas(top, width = 1000, height = 1000, bg = "black")
photo1 = PhotoImage(file = 'bg.gif')
topCanvas.create_image(500,350, image=photo1)
photo2 = PhotoImage(file = 'piano.gif')
#topCanvas.create_image(200,350, image=photo2)
photo3 = PhotoImage(file = 'drum.gif')
#topCanvas.create_image(500,350, image=photo3)
photo4 = PhotoImage(file = 'music.gif')
#topCanvas.create_image(800,350, image=photo4)
b1 = Button(topCanvas, image = photo2).pack(padx=0, pady=175, side=LEFT)
b2 = Button(topCanvas, image = photo3).pack(padx=0, pady=175, side=LEFT)
b3 = Button(topCanvas, image = photo4).pack(padx=0, pady=175, side=LEFT)
topCanvas.pack()


button = Button(root, text='Yah', bg='green', command=yahOrNah).pack(fill=X)
anotherButton = Button(root, text = 'Or Nah', bg = 'red', command=Quit).pack(fill=X)

root.mainloop()
