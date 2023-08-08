from tkinter import *

def move_up(event):
    canvas.move(myimage,0,-30)
def move_down(event):
    canvas.move(myimage,0,+30)
def move_left(event):
    canvas.move(myimage,-30,0)
def move_right(event):
    canvas.move(myimage,+30,0)

window = Tk()

window.bind("<w>",move_up)
window.bind("<s>",move_down)
window.bind("<a>",move_left)
window.bind("<d>",move_right)
window.bind("<Up>",move_up)
window.bind("<Down>",move_down)
window.bind("<Left>",move_left)
window.bind("<Right>",move_right)

canvas = Canvas(window,height=500,width=500)
canvas.pack()

bikeimage = PhotoImage(file='REFH bike.png')
myimage = canvas.create_image(0,0,image=bikeimage,anchor=NW)



window.mainloop()