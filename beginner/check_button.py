from tkinter import *


def display():
    if(x.get()==1):
    #if(x.get()):
    #if(x.get()=="YES"):
        print("you agree!")
    else:
        print("you dont agree :(")
window = Tk()

x = IntVar()
#x = BooleanVar()
#x = StringVar()
photo = PhotoImage(file='python.png')

check_button = Checkbutton(window,
                           text="I agree to something",
                           variable=x,
                           onvalue=1,
                           offvalue=0,
                           #onvalue=True,
                           #offvalue=False,
                           #onvalue="Yes",
                           #offvalue="No",
                           command=display,
                           font=('Arial',20),
                           fg="blue",
                           bg="green",
                           activebackground='green',
                           activeforeground='blue',
                           padx=25,
                           pady=10,
                           image=photo,
                           compound="left")
check_button.pack()

window.mainloop()