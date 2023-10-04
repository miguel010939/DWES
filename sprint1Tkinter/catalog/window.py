from tkinter import ttk
import tkinter as tk
from cell import Cell
from tkinter import messagebox

class MainWindow():
    def on_button_clicked(self, cell):
        message="Has hecho click en la celda "+ cell.title
        messagebox.showinfo("Información", message)
    
    def __init__(self, root):
        root.title("MainWindow")

        self.cells=[
            Cell("Animal 1", ".\\data\\unedited\\07CAT-STRIPES-mediumSquareAt3X-v2.jpg"),
            Cell("Animal 2", ".\\data\\unedited\\arctic_fox.jpg"),
            Cell("Animal 3", ".\\data\\unedited\\brown_bear.jpg"),
            Cell("Animal 4", ".\\data\\unedited\\koala.jpg"),
            Cell("Animal 5", ".\\data\\unedited\\red_panda.jpg")
        ]
        for i, cell in enumerate(self.cells):
            label=ttk.Label(root, image=cell.image, text=cell.title, compound=tk.BOTTOM)
            label.grid(row=0, column=i)
            label.bind("<Button-1>", lambda event, celda=cell: self.on_button_clicked(celda))
    


















