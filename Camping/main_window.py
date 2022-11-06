from tkinter import *
from PIL import Image, ImageTk
import random
import navigate_gui
import track_gui
import todo_gui
import os

window = Tk()

window.title("CAMPIFY")

# Center 
app_width = 400
app_height = 700

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = (screen_width / 2) - (app_width / 2)
y= (screen_height / 2) - (app_height / 2)

window.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')


img = ImageTk.PhotoImage(Image.open("C:\\Users\\alexi\\OneDrive\\Desktop\\Camping Images\\Window Background.png"))
my_label = Label(image=img)
my_label.img = img  # Save reference to image.
my_label.pack()

btn1 = Button(window, text = "Track a Friend", font='Helvetica 9 bold', padx = 20, pady = 15, command = lambda: track_gui.findFriendPage(window))
btn1.place(x=70, y=220)

btn2 = Button(window, text = "FInd a Camp Site", font='Helvetica 9 bold', padx = 15, pady = 15, command = lambda: navigate_gui.findCampPage(window))
btn2.place(x=210, y=220)

btn4 = Button(window, text = "To Do List", font='Helvetica 9 bold',padx = 34, pady = 15, command = lambda: todo_gui.toDoList(window))
btn4.place(x=135, y=290)




btn5 = Button(window, text="Exit", font='Helvetica 9 bold', padx = 15, pady = 5, command = window.quit)
btn5.place(x=160, y=630)

window.mainloop()

