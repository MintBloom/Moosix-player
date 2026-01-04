import tkinter
import customtkinter
from tkinter import filedialog, ttk
from tkinter import *
import os, pygame
import math, time
from threading import *

root = Tk()
root.title("Audio Player") #application title
root.geometry("700x700") #window startup size in pixels

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

class Music:
    def __init__(self, songs=[], current_song="", paused=False):
        self.songs = songs
        self.current_song = current_song # full path of the current song
        self.paused = paused

    def load_audio(self):
        #opens file manager to pick a folder
        root.directory = filedialog.askdirectory()
        for song in os.listdir(root.directory):
            name, ext = os.path.splitext(song)
            if ext in (".mp3", ".WAV", ".OGG"):
                full_path = os.path.join(root.directory, song)
                self.songs.append(full_path)
                audio_file_list.insert("end", song)
            # error handling here
        for song in self.songs:
            audio_file_list.insert("end", song)
        audio_file_list.selection_set(0)
        self.current_song = self.songs[audio_file_list.curselection()[0]]

    def play_audio(self):
        #play audio if not already playing
        self.threading()
        if not self.paused:
            pygame.mixer.music.load(self.current_song)
            pygame.mixer.music.play()
        else:
            pygame.mixer.music.unpause()
            self.paused = False

    def pause_audio(self):
        #pause audio
        pygame.mixer.music.pause()
        self.paused = True

    def next_track(self):
        #will update current song to the next song in the queue and play it
        try:
            audio_file_list.selection_clear(0, END)
            audio_file_list.selection_set(self.songs.index(self.current_song) + 1)
            self.current_song = self.songs[audio_file_list.curselection()[0]]
            self.play_audio()
        except:
            pass #if there is no next song, nothing will happen

    def previous_track(self):
        try:
            audio_file_list.selection_clear(0, END)
            audio_file_list.selection_set(self.songs.index(self.current_song) - 1)
            self.current_song = self.songs[audio_file_list.curselection()[0]]
            self.play_audio()
        except:
            pass

    def threading(self):
        t1 = Thread(target=self.audio_progress, daemon=True)
        t1.start

    def audio_progress(self):
        a = pygame.mixer.Sound(self.current_song)
        song_length = a.get_length()*3
        for i in range(0, math.ceil(song_length)):
            time.sleep(.4)
            progress_bar.set(pygame.mixer.music.get_pos() / 1000000)

music = Music()

#buttons
play_bttn = Button(control_frame, image=img_play_bttn, borderwidth=0, command=music.play_audio)
pause_bttn = Button(control_frame, image=img_pause_bttn, borderwidth=0, command=music.pause_audio)
next_bttn = Button(control_frame, image=img_next_bttn, borderwidth=0, command=music.next_track)
previous_bttn = Button(control_frame, image=img_previous_bttn, borderwidth=0, command=music.previous_track)

#progress bar
progress_bar = customtkinter.CTkProgressBar(master=root, progress_color='#32a85a', width=250)
progress_bar.place(relx=.5, rely=.95, anchor=tkinter.CENTER)

#actual buttons on the application window
play_bttn.grid(row=0, column=1, padx=1, pady=0)
pause_bttn.grid(row=0, column=2, padx=1, pady=0)
next_bttn.grid(row=0, column=3, padx=1, pady=0)
previous_bttn.grid(row=0, column=0, padx=1, pady=0)

organise_menu = Menu(menu_bar, tearoff=False) #organise menu created
menu_bar.add_cascade(label="Organise", menu=organise_menu) #organise menu added to menu bar
organise_menu.add_command(label="Select Audio Folder", command=music.load_audio) #command added to organise menu

if __name__=='__main__':
    root.mainloop()