
from tkinter import *
import os, pygame

root = Tk()
root.title("Audio Player") #application title
root.geometry("600x360") #window startup size in pixels

pygame.mixer.init() #allows audio to played

root.mainloop()
