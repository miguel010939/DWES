import tkinter as tk
from PIL import Image, ImageTk

class Cell:
    def __init__(self, title, path):
        self.title=title
        self.path=path
        self.image= ImageTk.PhotoImage(file=self.path)