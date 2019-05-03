import tkinter
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox

#from app import returnFiles, toPage

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

open = tkinter.Button(window, text = "Open", command=open_Dir_chooser())


open.grid(column=1, row=0)

# defining open_file_chooser function
combo = Combobox(window)

combo['values'] = ("java", "python", "c++")

combo.current(1)  # set the selected item

combo.grid(column=0, row=0)

window.mainloop()
#files, dir=returnFiles(Dir)
#rep=toPage(dir,files)

