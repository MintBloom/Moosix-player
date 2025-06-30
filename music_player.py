
from tkinter import *
import os, pygame

root = Tk()
root.title("Audio Player") #application title
root.geometry("600x360") #window startup size in pixels

pygame.mixer.init() #allows audio to played

audio_file_list = Listbox(root, bg="black", fg="white", width=100, height=16)
audio_file_list.pack()

#files used for corresponding commands in audio player
img_play_bttn = PhotoImage(file="Images/Play.png")
img_pause_bttn = PhotoImage(file="Images/Pause.png")
img_next_bttn = PhotoImage(file="Images/Next.png")
img_previous_bttn = PhotoImage(file="Images/Previous.png")

#tkinter frames which section the application window
control_frame = Frame(root)
control_frame.pack() 

#buttons
play_bttn = Button(control_frame, image=img_play_bttn, borderwidth=0)
pause_bttn = Button(control_frame, image=img_pause_bttn, borderwidth=0)
next_bttn = Button(control_frame, image=img_next_bttn, borderwidth=0)
previous_bttn = Button(control_frame, image=img_previous_bttn, borderwidth=0)

#actual buttons on the application window
play_bttn.grid(row=0, column=1, padx=1, pady=0)
pause_bttn.grid(row=0, column=2, padx=1, pady=0)
next_bttn.grid(row=0, column=3, padx=1, pady=0)
previous_bttn.grid(row=0, column=0, padx=1, pady=0)

root.mainloop()
