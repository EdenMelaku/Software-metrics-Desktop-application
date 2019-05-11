import tkinter
from tkinter import *
from tkinter import filedialog, scrolledtext
from tkinter.ttk import Combobox

#from app import returnFiles, toPage
import app
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
    txt.config(state='normal')
    txt.delete('1.0', END)


lbl = Label(window, text="welcome to software metrics application")

lbl.grid(column=0, row=0)



lbl = Label(window, text=" analysis report ")

lbl.grid(column=3, row=0)


open = tkinter.Button(window, text = "Choose project folder", command=open_Dir_chooser)


open.grid(column=0, row=2)


txt = scrolledtext.ScrolledText(window,width=100,height=30)

txt.grid(column=3, row=6)




txtt = scrolledtext.ScrolledText(window,width=50,height=30)

txtt.grid(column=0, row=6)






txtt.config(state='disable')


# defining open_file_chooser function
combo = Combobox(window)

combo['values'] = ("java", "python", "c++")
vals=["java", "python", "c++"]

combo.current(1)  # set the selected item

combo.grid(column=0, row=3)
def send():
 txt.config(state='normal')
 app.initReport(Dir)
 x="GENERATING REPORT FOR THE PROJECT FOLDER    "+Dir+"\n\n\n";
 txt.insert(INSERT, x)

 files, dir=returnFiles(Dir)
 print(combo.get())
 print("INSIDE METHOD")
 rep=toPage(dir,files,combo.get())
 txt.insert(INSERT, rep)
 txt.config(state='disable')

open = tkinter.Button(window, text = "analyse", command=send)


open.grid(column=0, row=4)
window.mainloop()

