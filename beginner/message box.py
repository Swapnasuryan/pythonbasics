from tkinter import *
from tkinter import messagebox    # import messagebox library

def click():
#    messagebox.showinfo(title='This is an info message box',message='You are a person')
#   while(True):
#         messagebox.showwarning(title='Warning', message='You have a Virus!!!!')
#   messagebox.showerror(title='Error', message='Something went wrong: ')
#    if messagebox.askokcancel(title='ask ok cancel',message='Do you want to do the thing?'):
#        print("You did a thing!")
#    else:
#        print('You cancel a thing!')

#    if messagebox.askretrycancel(title='ask ok cancel', message='Do you want to retry the thing?'):
#        print("You retry a thing!")
#    else:
#        print('You canceled a thing!')

#    if messagebox.askyesno(title='ask yes or no',message='Do you like  cake'):
#        print("I like cake too ")
#    else:
#        print("Why do you not like cake")

#    answer = messagebox.askquestion(title='ask question',message='Do you like coke?')
#    if(answer == 'yes'):
#        print("I like coke too!")
#    else:
#       print("Why don't you like?")
    answer = messagebox.askyesnocancel(title='yes no cancel',message='Do you like this code',icon='info')
    if(answer==True):
        print("you like to code")
    elif(answer==False):
       print("Then why are you watching a video on coding?")
    else:
       print("You have dodged the question")






window = Tk()

button =Button(window,command=click,text="click me")
button.pack()

window.mainloop()
