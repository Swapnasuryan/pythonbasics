# widgets = GUI elements: buttons, textboxes, labels, images
# windows = serves as a container to hold or contain these widgets

#window = Tk()  #instantiate an istance of a window
#window.geometry("420x420")
#window.title("Swapna Suryan first GUI program")

#icon = PhotoImage(file='ILTQq.png')
#window.iconphoto(True,icon)
#window.config(background="black")
#window.config(background="#630cab")

#window.mainloop() # place window on computer screen, listen for events

#label = an area widget that holds text and/or an image within a window

window = Tk()

photo = PhotoImage(file='ILTQq.png')
label = Label(window,
              text="Hello World",
              font=('Arial',40,'bold'),
              fg='green',
              bg='black',
              relief=RAISED,
              bd=10,
              padx=20,
              pady=20,
              image=photo)
label.pack()
#label.place(x=0,y=0)
window.mainloop()