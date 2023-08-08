# radio button = similar to checkbox, but you can only select one from a group
from tkinter import *

food = ["Pizza","Biryani","Burger"]
def order():
    if (x.get()==0):
        print("You ordered pizza!")
    elif(x.get()==1):
        print("You ordered Biryani!")
    elif(x.get()==2):
        print("you ordered Burger!")
    else:
        print("huh?!")
window = Tk()

pizzaImage = PhotoImage(file='pizza.png')
biryaniImage = PhotoImage(file='biryani.png')
burgerImage = PhotoImage(file='burger.png')
foodimages = [pizzaImage,biryaniImage,burgerImage]

x = IntVar()
for index in range(len(food)):
    radiobutton = Radiobutton(window,
                              text=food[index],  #adds text to radio buttons
                              variable=x,        #groups radiobuttons together if they share the same variable
                              value=index,       # assigns each radiobutton a different value
                              padx=25,           #adds padding on x-axis
                              pady=30,
                              font=("Impact",10),
                              image=foodimages[index],  #add image to radiobutton
                              compound='left',          #adds image & text (left-side)
                              indicatoron=0,            #eliminate circle indicators
                              width=375,               # sets width of radio buttons
                              command=order)
    radiobutton.pack(anchor='w')


window.mainloop()