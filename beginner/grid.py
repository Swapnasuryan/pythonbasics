from tkinter import *

#grid() = geometry manager that organizes widgets in a table-like structure in a parent

#def submit():


window = Tk()

titleLabel = Label(window,text="Enter your info: ",font=("Arial",25)).grid(row=0,column=0,columnspan=2)

firstNameLabel = Label(window,text="First name: ",width=20,bg="red").grid(row=1,column=0)
firstNameEntry = Entry(window).grid(row=1,column=1)

lastNameLabel = Label(window,text="Last name: ",width=20, bg="green").grid(row=2,column=0)
lastNameEntry = Entry(window).grid(row=2,column=1)

emailLabel = Label(window,text="E-mail: ",width=20,bg="blue").grid(row=3,column=0)
emailEntry = Entry(window).grid(row=3,column=1)

submitButton = Button(window,text="submit").grid(row=4,column=0,columnspan=2)



window.mainloop()