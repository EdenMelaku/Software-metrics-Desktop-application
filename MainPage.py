from tkinter import *

window = Tk()

window.title("SOFTWARE METRICS APPLICATION")

window.geometry('350x200')

lbl = Label(window, text="welcome to software metrics application")

lbl.grid(column=0, row=0)

btn = Button(window, text="Click Me")

btn.grid(column=1, row=0)

window.mainloop()