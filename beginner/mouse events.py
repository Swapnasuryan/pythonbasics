from tkinter import *

def mouse(event):
    print("The mouse works: "+str(event.x)+","+str(event.y))
window = Tk()

#window.bind("<Button-1>", mouse)   #left mouse click
#window.bind("<Button-2>", mouse)   #scroll
#window.bind("<Button-3>", mouse)    #right click
#window.bind("<ButtonRelease>",mouse)
#window.bind("<Enter>",mouse)  # enter the window
#window.bind("<Leave>",mouse)   #leave the window
#window.bind("<Motion>",mouse)      #where the mouse moved

window.mainloop()