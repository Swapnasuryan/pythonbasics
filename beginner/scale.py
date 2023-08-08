from tkinter import *

def submit():
    print("The temperature is: "+str(scale.get())+" degree celsius")


window = Tk()

hotImage = PhotoImage(file='hot.png')
hotlabel = Label(image=hotImage)
hotlabel.pack()


scale = Scale(window,
              from_=100,
              to=0,
              length=600,
              orient=VERTICAL,         # orientation of scale
              font=('consolas',20),
              tickinterval=10,          #adds numeric indicators for value
              showvalue=0,              #hide current value
              resolution=5,            #increment of slider
              troughcolor='#69EAFF',
              fg='red',
              bg='black',
              )
scale.set(((scale['from']-scale['to'])/2)+scale['to'])      #set current value of slider
scale.pack()

coldImage = PhotoImage(file='cold.png')
coldlabel = Label(image=coldImage)
coldlabel.pack()

button = Button(window,text='submit',command=submit)
button.pack()
window.mainloop()