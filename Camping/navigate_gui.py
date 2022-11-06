from tkinter import *
from PIL import Image, ImageTk
import tkinter
import tkintermapview
import random
import os


def findCampPage(window):
        #global opened, firstWindow
  
        firstWindow = tkinter.Toplevel(window)  # Create new window.

        firstWindow.title("CAMPIFY")

        # Change Icon photo
        #image = PhotoImage(file = "C:\\Users\\alexi\\Desktop\\Project Photos\\Dice logo.png")
        #firstWindow.iconphoto(False, image)

        # Center 
        app_width = 400
        app_height = 700

        screen_width = firstWindow.winfo_screenwidth()
        screen_height = firstWindow.winfo_screenheight()

        x = (screen_width / 2) - (app_width / 2)
        y= (screen_height / 2) - (app_height / 2)

        firstWindow.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')


        def find():
               
               map.set_address(my_entry.get())
               map.set_marker(my_entry.get())


        my_lbl = LabelFrame(firstWindow)
        my_lbl.pack(pady = 20)

        my_frame = LabelFrame(firstWindow)
        my_frame.pack(pady = 10)


        map = tkintermapview.TkinterMapView(my_lbl, width=400, height=600, corner_radius=0)
        map.pack()
        

        map.set_position(40.7423, -74.1793)
        marker_0 = map.set_marker(40.7423, -74.1793, text="NJIT")

        marker_1 = map.set_marker(40.9705, -75.0728, text="Great Divide Campground")
        marker_2 = map.set_marker(40.99578660, -74.77870380, text="Harmony Ridge Farm & Camp Ground")
        marker_3 = map.set_marker(41.1905557, -74.7479701, text="Harmony Ridge Farm & Camp Ground")
        marker_4 = map.set_marker(41.19030860, -74.73060250, text="Kymer's Camping Resort")
        marker_5 = map.set_marker(40.7120409, -74.0438809, text="Liberty Harbor RV Park")
        marker_6 = map.set_marker(41.03499510, -75.00158600, text="Mohican Outdoor Center")
        marker_7 = map.set_marker(40.9621856, -74.7362144, text="Panther Lake Camping")
        marker_8 = map.set_marker(41.27426, -74.638901, text="Pleasant Acres Farm Campground")
        marker_9 = map.set_marker(40.09921550, -74.30372360, text="Butterfly Camping Resort")
        marker_10 = map.set_marker(40.616163, -75.065062, text="Mountain View Campground")
        marker_11 = map.set_marker(40.1794, -74.27553, text="Pine Cone Resort")
        marker_12 = map.set_marker(40.1017,  -74.2728, text="Tip Tam Camping Resort")
        marker_13 = map.set_marker(39.53879291, -75.27810589, text="Adventure Bound Tall Pines")
        marker_14 = map.set_marker(39.63474500, -74.31409800, text="Baker's Acres Campground")
        marker_15 = map.set_marker(39.00456610, -74.89262790, text="Beachcomber Camping Resort")
        marker_16 = map.set_marker(39.61872290 , -74.59718520, text="Belhaven Resort & Campground")
        marker_17 = map.set_marker(39.61659600 , -75.27545600 , text="Four Seasons Family Campground")
        marker_18 = map.set_marker(39.1812, -74.7314, text="Ocean View Resort")
        marker_19 = map.set_marker(39.55475, -74.80952, text="Roamers Beach RV Resort")
        marker_20 = map.set_marker(38.94488850, -74.93200150 , text="The Depot Travel Park")
        marker_21 = map.set_marker(39.630294319394, -74.480808084214, text="Timberline Lake Camping Resort")
        marker_22 = map.set_marker(39.6123749957, -74.5004863018, text="Turtle Run Campground")
        marker_23 = map.set_marker(39.68812, -74.54472, text="Wading Pines Camping Resort")
        marker_24 = map.set_marker(39.4921357, -74.7717261, text="Winding River Campground")

        #def path():
        path_1 = map.set_path([marker_0.position, marker_1.position, (40.7423, -74.1793), (40.9705, -75.0728)])
        path_2 = map.set_path([marker_0.position, marker_2.position, (40.7423, -74.1793), (40.99578660, -74.77870380)])
        path_3 = map.set_path([marker_0.position, marker_3.position, (40.7423, -74.1793), (41.1905557, -74.7479701)])
        path_4 = map.set_path([marker_0.position, marker_4.position, (40.7423, -74.1793), (41.19030860, -74.73060250)])
        path_5 = map.set_path([marker_0.position, marker_5.position, (40.7423, -74.1793), (40.7120409, -74.0438809)])
        path_6 = map.set_path([marker_0.position, marker_6.position, (40.7423, -74.1793), (41.03499510, -75.00158600)])
        path_7 = map.set_path([marker_0.position, marker_7.position, (40.7423, -74.1793), (40.9621856, -74.7362144)])
        path_8 = map.set_path([marker_0.position, marker_8.position, (40.7423, -74.1793), (41.1905557, -74.7479701)])
        path_9 = map.set_path([marker_0.position, marker_9.position, (40.7423, -74.1793), (40.09921550, -74.30372360)])
        path_10 = map.set_path([marker_0.position, marker_10.position, (40.7423, -74.1793), (40.616163, -75.065062)])
        path_11 = map.set_path([marker_0.position, marker_11.position, (40.7423, -74.1793), (40.1794, -74.27553)])
        path_12 = map.set_path([marker_0.position, marker_12.position, (40.7423, -74.1793), (40.1017,  -74.2728)])
        path_13 = map.set_path([marker_0.position, marker_13.position, (40.7423, -74.1793), (39.53879291, -75.27810589)])
        path_14 = map.set_path([marker_0.position, marker_14.position, (40.7423, -74.1793), (39.63474500, -74.31409800)])
        path_15 = map.set_path([marker_0.position, marker_15.position, (40.7423, -74.1793), (39.00456610, -74.89262790)])
        path_16 = map.set_path([marker_0.position, marker_16.position, (40.7423, -74.1793), (39.61872290 , -74.59718520)])
        path_17 = map.set_path([marker_0.position, marker_17.position, (40.7423, -74.1793), (39.61659600 , -75.27545600)])
        path_18 = map.set_path([marker_0.position, marker_18.position, (40.7423, -74.1793), (39.1812, -74.7314)])
        path_19 = map.set_path([marker_0.position, marker_19.position, (40.7423, -74.1793), (39.55475, -74.80952)])
        path_20 = map.set_path([marker_0.position, marker_20.position, (40.7423, -74.1793), (38.94488850, -74.93200150)])
        path_21 = map.set_path([marker_0.position, marker_21.position, (40.7423, -74.1793), (39.630294319394, -74.480808084214)])
        path_22 = map.set_path([marker_0.position, marker_22.position, (40.7423, -74.1793), (39.6123749957, -74.5004863018)])
        path_23 = map.set_path([marker_0.position, marker_23.position, (40.7423, -74.1793), (39.68812, -74.54472)])
        path_24 = map.set_path([marker_0.position, marker_24.position, (40.7423, -74.1793), (39.4921357, -74.7717261)])



        my_entry = Entry(my_frame, font = ("Helvetica", 8))
        my_entry.grid(row = 0, column = 0, padx = 10, pady = 5)

        btn1 = Button(my_frame, text = "Search",font = ("Helvetica", 8), command = find )
        btn1.grid(row = 0, column = 1, padx = 10)

        btn2 = Button(my_frame, text="Back", font='Helvetica 9 bold', padx = 5, pady = 5, command = findCampPage.destroy)
        btn2.place(x=160, y=630)

        







   


      