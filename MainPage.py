import tkinter
from tkinter import *
from tkinter import filedialog, scrolledtext
from tkinter.ttk import Combobox

#from app import returnFiles, toPage
from app import returnFiles, toPage

window = Tk()

window.title("SOFTWARE METRICS APPLICATION")

window.geometry('1200x600')
Dir=""
def open_Dir_chooser():
    ProjDir = filedialog.askdirectory()
    global Dir
    Dir=ProjDir
    print("You have selected : %s" % ProjDir)

lbl = Label(window, text="welcome to software metrics application")

lbl.grid(column=0, row=0)

open = tkinter.Button(window, text = "Choose project folder", command=open_Dir_chooser)


open.grid(column=3, row=0)


txt = scrolledtext.ScrolledText(window,width=140,height=30)

txt.grid(column=4, row=6)


# defining open_file_chooser function
combo = Combobox(window)

combo['values'] = ("java", "python", "c++")
vals=["java", "python", "c++"]

combo.current(1)  # set the selected item

combo.grid(column=0, row=3)
def send():
 files, dir=returnFiles(Dir)
 print(combo.get())
 print("INSIDE METHOD")
 rep=toPage(dir,files,combo.get())
 txt.insert(INSERT, rep)

open = tkinter.Button(window, text = "analyse", command=send)


open.grid(column=3, row=3)
window.mainloop()

