import pygame.mixer as mixer
import os
import tkinter
from tkinter import Button
from tkinter import filedialog

mixer.init()

def loadSong():
    mixer.music.load(filedialog.askopenfilename())

def playSong():
    mixer.music.play

def pauseSong():
    mixer.music.pause()

def musicPage(window):
    #global opened, firstWindow
  
    musicWindow = tkinter.Toplevel(window)  # Create new window.

    musicWindow.title("CAMPIFY Music Player")

    # Change Icon photo
    #image = PhotoImage(file = "C:\\Users\\alexi\\Desktop\\Project Photos\\Dice logo.png")
    #firstWindow.iconphoto(False, image)

    # Center 
    app_width = 400
    app_height = 700

    screen_width = musicWindow.winfo_screenwidth()
    screen_height = musicWindow.winfo_screenheight()

    x = (screen_width / 2) - (app_width / 2)
    y= (screen_height / 2) - (app_height / 2)

    musicWindow.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

    open_button = Button(musicWindow, text = "Open a music file", font = "Helvetic 9 bold", padx = 15, pady = 15, command = loadSong)
    open_button.place(x = 70, y = 240)

    play_button = Button(musicWindow, text = "Play file", font = "Helvetic 9 bold", padx = 15, pady = 15, command = playSong)
    play_button.place(x = 240, y = 240)
    
    play_button = Button(musicWindow, text = "Pause song", font = "Helvetic 9 bold", padx = 15, pady = 15, command = pauseSong)
    play_button.place(x = 240, y = 340)


