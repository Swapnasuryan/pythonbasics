from tkinter import *
from tkinter import colorchooser    #submodule

def clcik():
#    color = colorchooser.askcolor()
#    print(color)
#    colorHex = color[1]
#    print(colorHex)
#    window.config(bg=color[1])
#    window.config(bg=colorchooser.askcolor()[1])   #one line code to change background color
window = Tk()
window.geometry("420x420")
button = Button(text='click me',command=clcik)
button.pack()

window.mainloop()