import tkinter as tk
from PIL import Image, ImageTk

class Cell:
    def __init__(self, title, path):
        self.title=title
        self.path=path
        original=Image.open(fp=self.path)
        rescaled=original.resize((100, 100))
        # Si escribo Image.ANTIALIAS, python me devuelve:
        # AttributeError: module 'PIL.Image' has no attribute 'ANTIALIAS'
        # Asi, al menos funciona
        self.image=ImageTk.PhotoImage(rescaled)