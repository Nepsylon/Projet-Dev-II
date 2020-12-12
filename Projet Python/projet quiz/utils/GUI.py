from tkinter import *
from utils.operations import *


def interface_graphique():
    window = Tk()

    window.title("Projet Questions pour un champion")
    window.config(background='#8DE7C1')
    window.minsize(480, 360)

    frame = Frame(window, bg='#8DE7C1')

    champ_label = Label(frame, text='Bienvenue dans notre projet quiz !', font=("Calibri", 25), bg='#8DE7C1',
                        fg='white')
    champ_label.pack()

    bouton = Button(frame, text='commencer', command=display_cat(table_cat))
    bouton.pack()

    frame.pack(expand=YES)
    window.mainloop()
