from tkinter import *
import time

WIDTH = 5000
HEIGHT = 5000
xVelocity = 2
yvelocity = 3

window = Tk()

canvas = Canvas(window,width=WIDTH,height=HEIGHT)
canvas.pack()

backgroundImage = PhotoImage(file='space.png')
background = canvas.create_image(0,0,image=backgroundImage,anchor=NW)

spaceImage = PhotoImage(file='spacecraft.png')
my_image = canvas.create_image(0,0,image=spaceImage,anchor=NW)

image_width = spaceImage.width()
image_height = spaceImage.height()

while True:
    coordinates = canvas.coords(my_image)
    print(coordinates)
    if (coordinates[0] >= (WIDTH-image_width) or coordinates[0] < 0):
        xVelocity = -xVelocity
    if (coordinates[1] >= (HEIGHT-image_height) or coordinates[1] < 0):
        yvelocity = -yvelocity
    canvas.move(my_image,xVelocity,yvelocity)

    window.update()
    time.sleep(0.01)

window.mainloop()