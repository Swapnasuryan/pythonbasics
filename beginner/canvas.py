# canvas = widget that is used to draw graphs,plots,images in a window

from tkinter import *


window = Tk()

canvas = Canvas(window,height=500,width=500)
#canvas.create_line(0,0,500,500,fill='blue',width=5)
#canvas.create_line(0,500,500,0,fill='red',width=5)
#canvas.create_rectangle(50,50,300,300,fill='purple')
#points = [250,0,500,500,0,500]
#canvas.create_polygon(points,fill='yellow',width=5)
#canvas.create_polygon(250,0,500,500,0,500,fill='yellow',outline="black",width=5)
#canvas.create_arc(0,0,500,500,fill="green",start=20,extent=270,width=5)
canvas.create_arc(0,0,500,500,fill='#f31f1f',extent=180,width=10)
canvas.create_arc(0,0,500,500,fill='white',extent=180,start=180,width=10)
canvas.create_oval(190,190,310,310,fill='white',width=10)
canvas.pack()


window.mainloop()