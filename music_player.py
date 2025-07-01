from tkinter import filedialog
from tkinter import *
import os, pygame

root = Tk()
root.title("Audio Player") #application title
root.geometry("700x400") #window startup size in pixels

pygame.mixer.init() #allows audio to played

#menu bar added to root window
menu_bar = Menu(root)
root.config(menu=menu_bar)

audio_file_list = Listbox(root, bg="black", fg="white", width=100, height=16)
audio_file_list.pack()

#tkinter frames which section the application window
control_frame = Frame(root)
control_frame.pack()

#files used for corresponding commands in audio player
img_play_bttn = PhotoImage(file="Images/Play.png")
img_pause_bttn = PhotoImage(file="Images/Pause.png")
img_next_bttn = PhotoImage(file="Images/Next.png")
img_previous_bttn = PhotoImage(file="Images/Previous.png")

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

class Music:
    def __init__(self, songs=[], current_song="", paused=False):
        self.songs = songs
        self.current_song = current_song
        self.paused = paused

    def load_audio(self):
        #opens file manager to pick a folder
        root.directory = filedialog.askdirectory()
        for song in os.listdir(root.directory):
            ext = os.path.splitext(song)
            if ext in (".mp3", ".mp4"):
                self.songs.append(song)
            # error handling here
        for song in self.songs:
            audio_file_list.insert("end", song)
        audio_file_list.selection_set(0)
        self.current_song = self.songs[audio_file_list.curselection()] #TypeError here

music = Music()

organise_menu = Menu(menu_bar, tearoff=False) #organise menu created
menu_bar.add_cascade(label="Organise", menu=organise_menu) #organise menu added to menu bar
organise_menu.add_command(label="Select Audio Folder", command=music.load_audio) #command added to organise menu

if __name__=='__main__':
    root.mainloop()
