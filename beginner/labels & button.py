# label = an area widget that holds text and/or an image within a window
from tkinter import *
#window = Tk()

#photo = PhotoImage(file='ILTQq.png')
#label = Label(window,
#              text="Hey I'am a Penguin",
#              font=('Arial',40,'bold'),
#              fg='green',
#              bg='black',
#              relief=RAISED,
#              bd=10,
#              padx=20,
#              pady=20,
#              image=photo,
#              compound='bottom')
#label.pack()
#label.place(x=0,y=0)
#window.mainloop()


# button = you click it, then it does stuff

window = Tk()

count = 0
def click():
    global count
    count+=1
    print(count)
#    print("you clciked the button!")

photo = PhotoImage(file='thumbsup.png')
button = Button(window,
                text="click me!",
                command=click,
                font=("comic sans",30),
                fg="red",
                bg="black",
                activeforeground="red",
                activebackground="black",
                state=ACTIVE,
                image=photo,
                compound="bottom")
button.pack()

window.mainloop()