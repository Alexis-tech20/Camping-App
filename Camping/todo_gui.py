from tkinter import *
from PIL import Image, ImageTk
import tkinter
import tkintermapview
import random
import os
import pickle
from tkinter.font import Font
from tkinter import filedialog 


def toDoList(window):

    thirdWindow = tkinter.Toplevel(window)  # Create new window.

    thirdWindow.title("CAMPIFY")

    app_width = 500
    app_height = 700

    screen_width = thirdWindow.winfo_screenwidth()
    screen_height = thirdWindow.winfo_screenheight()

    x = (screen_width / 2) - (app_width / 2)
    y= (screen_height / 2) - (app_height / 2)

    thirdWindow.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

    thirdWindow['bg']='green'

    # Define our Font
    my_font = Font(
        family="Brush Script MT",
        size=30,
        weight="bold")

    # Create frame
    my_frame = Frame(thirdWindow)
    my_frame.pack(pady=10)

    
    # Create listbox
    My_list = Listbox(my_frame,
        font=my_font,
        width=25,
        height=5,
        bg="SystembuttonFace",
        bd=0,
        fg="#464646",
        highlightthickness=0,
        selectbackground="#a6a6a6",
        activestyle="none")


    My_list.pack(side=LEFT, fill=BOTH)

    # Create dummy list
    stuff = ["Set Up Tent", "Track Friend", "Make smores", "Finish Project", "Get Some Sleep" ]
    # Add dummy list to list box
    for item in stuff:
        My_list.insert(END, item)

    # Create scrollbar
    my_scrollbar = Scrollbar(my_frame)
    my_scrollbar.pack(side=RIGHT, fill=BOTH)

    # Add scrollbar
    My_list.config(yscrollcommand=my_scrollbar.set)
    my_scrollbar.config(command=My_list.yview)

    # Create entry box to add items to the listMy_list
    my_entry = Entry(thirdWindow, font=("Helvetica", 24), width= 26)
    my_entry.pack(pady=20)

    # Create a button frame 
    button_frame = Frame(thirdWindow)
    button_frame.pack(pady=20)

    # FUNCTIONS
    def delete_item():
        My_list.delete(ANCHOR)

    def add_item():
        My_list.insert(END, my_entry.get())
        my_entry.delete(0, END)
    def uncross_item():
        My_list.itemconfig(
        My_list.curselection(),
        fg= "#464646")
        My_list.selection_clear(0, END)

    #def file_name():

    
    def crossoff_item():
        My_list.itemconfig(My_list.curselection(),fg= "#dedede")

    def delete_crossed():
        My_list.delete(ANCHOR)

    def save_list():
        file_name = filedialog.asksaveasfilename(
            initialdir= "C:/gui/data",
            title= "Save File",
            filetypes=(("Dat Files", "*.dat"),
                        ("All Files", "*.*"))
            )

        if file_name:
            if file_name.endswith(".dat"):
                pass
            else:
                file_name = f'{file_name}.dat'

    def file_name():

    # grab all stuff from the list
        stuff = My_list.get(0, END)

        # Open the file
        output_file = open(file_name, 'wb')

    #actually add the stuff
        pickle.dump(stuff, output_file)

    def open_list():
        file_name = filedialog.asksaveasfilename(
            initialdir= "C:/gui/data",
            title= "Save File",
            filetypes=(("Dat Files", "*.dat"),
                        ("All Files", "*.*"))
        )


    def delete_list():
        My_list.delete(0, END)

    # Create menu
    my_menu= Menu(thirdWindow)
    thirdWindow.config(menu=my_menu)

    # Add items to menu
    file_menu = Menu(my_menu, tearoff=False)
    my_menu.add_cascade(label="File", menu=file_menu)
    # Add dropdown items
    file_menu.add_command(label="Save_list", command=save_list)
    file_menu.add_command(label="Open_list", command=open_list)
    file_menu.add_separator()
    file_menu.add_command(label="Clear_list", command=delete_list)


    # add some buttons 
    delete_button= Button(button_frame, text="Delete Item", command=delete_item)
    add_button= Button(button_frame, text="Add Item", command=add_item)
    cross_off_button= Button(button_frame, text="Cross Off Item", command=crossoff_item)
    uncross_button= Button(button_frame, text="Uncross Item", command=uncross_item)
    delete_crossed_button= Button(button_frame, text="Delete Crossed", command=delete_crossed)
    destroy_window_button = Button(button_frame, text = "Back", command = thirdWindow.destroy)

   

    delete_button.grid(row=0,column=0)
    add_button.grid(row=0,column=1, padx=20)
    cross_off_button.grid(row=0,column=2)
    uncross_button.grid(row=0,column=3, padx=20)
    delete_crossed_button.grid(row=0,column=4)
    destroy_window_button.grid(rowspan=9,columnspan=20)


