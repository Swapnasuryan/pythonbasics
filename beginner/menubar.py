from tkinter import *

def openfile():
    print("file has been opened")
def savefile():
    print("file has been saved")
def cut():
    print("you cut some text!")
def copy():
    print("you copied some text!")
def paste():
    print("you pasted some text")
window = Tk()

openImage = PhotoImage(file='open.png')
saveImage = PhotoImage(file='save.png')
exitImage = PhotoImage(file='exit.png')

menubar = Menu(window)
window.config(menu=menubar)

fileMenu = Menu(menubar,tearoff=0,font=("mv boli",15))
menubar.add_cascade(label="File",menu=fileMenu)
fileMenu.add_command(label="Open",command=openfile,image=openImage,compound='left')
fileMenu.add_cascade(label="save",command=savefile,image=saveImage,compound='left')
fileMenu.add_separator()
fileMenu.add_command(label="Exit",command=quit,image=exitImage,compound='left')

editMenu = Menu(menubar,tearoff=0,font=("mv boli",15))
menubar.add_cascade(label="Edit",menu=editMenu)
editMenu.add_command(label="cut",command=cut)
editMenu.add_command(label="copy",command=copy)
editMenu.add_command(label="paste",command=paste)

window.mainloop()