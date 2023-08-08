from tkinter import *
from tkinter import filedialog

def openfile():
    filepath = filedialog.askopenfilename(initialdir="C:\\Users\\nagen\\PycharmProjects\\beginner",
                                          title="open file okay? ",
                                          filetypes= (("text files","*.txt"),
                                          ("all files","*.*")))
#    print(filepath)
    file = open(filepath,'r')
    print(file.read())
    file.close()
window = Tk()
button = Button(window,text="open",command=openfile)
button.pack()

window.mainloop()