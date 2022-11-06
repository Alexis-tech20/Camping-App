from tkinter import *
from PIL import Image, ImageTk
import tkinter
import tkintermapview
import random
import os


def findFriendPage(window):
        #global opened, firstWindow
  
        secondWindow = tkinter.Toplevel(window)  # Create new window.

        secondWindow.title("CAMPIFY")

        # Change Icon photo
        #image = PhotoImage(file = "C:\\Users\\alexi\\Desktop\\Project Photos\\Dice logo.png")
        #firstWindow.iconphoto(False, image)

        # Center 
        app_width = 400
        app_height = 700

        screen_width = secondWindow.winfo_screenwidth()
        screen_height = secondWindow.winfo_screenheight()

        x = (screen_width / 2) - (app_width / 2)
        y= (screen_height / 2) - (app_height / 2)

        secondWindow.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')


        def find():
               
               map.set_address(my_entry.get())
               map.set_marker(my_entry.get())


        my_lbl = LabelFrame(secondWindow)
        my_lbl.pack(pady = 20)

        my_frame = LabelFrame(secondWindow)
        my_frame.pack(pady = 10)


        map = tkintermapview.TkinterMapView(my_lbl, width=400, height=600, corner_radius=0)
        map.pack()
        

        map.set_position(40.7423, -74.1793)
        marker_0 = map.set_marker(40.7423, -74.1793, text="NJIT")

        marker_1 = map.set_marker(40.9705, -75.0728, text="Karen")
        marker_2 = map.set_marker(40.99578660, -74.77870380, text="Alizaya")
        marker_3 = map.set_marker(41.1905557, -74.7479701, text="Ryan")
        marker_4 = map.set_marker(41.19030860, -74.73060250, text="Kevin")
        marker_5 = map.set_marker(40.7120409, -74.0438809, text="Goodness")


        #def path():
        path_1 = map.set_path([marker_0.position, marker_1.position, (40.7423, -74.1793), (40.9705, -75.0728)])
        path_2 = map.set_path([marker_0.position, marker_2.position, (40.7423, -74.1793), (40.99578660, -74.77870380)])
        path_3 = map.set_path([marker_0.position, marker_3.position, (40.7423, -74.1793), (41.1905557, -74.7479701)])
        path_4 = map.set_path([marker_0.position, marker_4.position, (40.7423, -74.1793), (41.19030860, -74.73060250)])
        path_5 = map.set_path([marker_0.position, marker_5.position, (40.7423, -74.1793), (40.7120409, -74.0438809)])




        my_entry = Entry(my_frame, font = ("Helvetica", 8))
        my_entry.grid(row = 0, column = 0, padx = 10, pady = 5)

        btn1 = Button(my_frame, text = "Search",font = ("Helvetica", 8), command = find )
        btn1.grid(row = 0, column = 1, padx = 10)

        btn2 = Button(my_frame, text="Back", font='Helvetica 9 bold', padx = 5, pady = 5, command = findFriendPage.destroy)
        btn2.place(x=160, y=630)
