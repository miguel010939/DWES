import tkinter as tk
from tkinter import Tk
from PIL import Image, ImageTk
from detail_window import DetailWindow

class Cell:
     
    def __init__(self, title, path, description="No description available"):
        self.title=title
        self.path=path
        self.description=description
        original=Image.open(fp=self.path)
        rescaled=original.resize((100, 100))
        # Si escribo Image.ANTIALIAS, python me devuelve:
        # AttributeError: module 'PIL.Image' has no attribute 'ANTIALIAS'
        # Asi, al menos funciona
        self.image=ImageTk.PhotoImage(rescaled)