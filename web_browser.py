#**********     imports     **********
import tkinter as tk
from tkinter import *
import webbrowser

#**********     classes     **********
class Window(Frame):
    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.master = master

#**********     functions     **********
def google():
    webbrowser.open("www.google.com")

def youtube():
    webbrowser.open("www.youtube.com")

def github():
    webbrowser.open("www.github.com")

#**********     Main     **********
root = Tk()
app = Window(root)

root.wm_title("JKBrowser")
root.geometry("300x300+20+20")
root.minsize(300,300)
root.maxsize(300,300)

igoogle = PhotoImage(file="images/google.png")
google = tk.Button(root, image = igoogle, command = google)
google.grid(row = 0, column = 0, pady = 5, padx = 10)


iyoutube = PhotoImage(file="images/youtube.png")
youtube = tk.Button(root, image = iyoutube, command = youtube)
youtube.grid(row = 0, column = 1, pady = 5, padx = 10)

igithub = PhotoImage(file="images/github.png")
github = tk.Button(root, image = igithub, command = github)
github.grid(row = 1, column = 0, pady = 5, padx = 10)

root.mainloop()
