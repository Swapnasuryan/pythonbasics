# listbox = a listing of selectable text items within it's own container

def submit():
    food = []
    for index in listbox.curselection():
        food.insert(index,listbox.get(index))
    print("You have ordered: ")
    for index in food:
        print(index)
#    print(listbox.get(listbox.curselection()))   # for single item selection

def add():
    listbox.insert(listbox.size(),entryBox.get())
    listbox.config(height=listbox.size())

def delete():
    for index in reversed(listbox.curselection()):
        listbox.delete(index)

#    print(listbox.delete(listbox.curselection()))    # for single item selection
    listbox.config(height=listbox.size())


from tkinter import *

window = Tk()

listbox = Listbox(window,
                  bg="#f7ffde",
                  font=("constantia",35),
                  width=12,
                  selectmode=MULTIPLE)
listbox.pack()

listbox.insert(1,"Pizza")
listbox.insert(2,"Pasta")
listbox.insert(1,"garlic bread")
listbox.insert(1,"soup")
listbox.insert(1,"salad")

listbox.config(height=listbox.size())

entryBox = Entry(window)
entryBox.pack()

submit_button = Button(window,
                       text="submit",command=submit)
submit_button.pack()

addButton = Button(window,text="add",command=add)
addButton.pack()

deleteButton = Button(window,text="Delete",command=delete)
deleteButton.pack()

window.mainloop()