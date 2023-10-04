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
            Cell("Animal 1", ".\\data\\edited\\arctic_fox_100x100.png"),
            Cell("Animal 2", ".\\data\\edited\\brown_bear_100x100.png"),
            Cell("Animal 3", ".\\data\\edited\\cat_100x100.png"),
            Cell("Animal 4", ".\\data\\edited\\koala_100x100.png"),
            Cell("Animal 5", ".\\data\\edited\\red_panda_100x100.png")
        ]
        for i, cell in enumerate(self.cells):
            label=ttk.Label(root, image=cell.image, text=cell.title, compound=tk.BOTTOM)
            label.grid(row=0, column=i)
            label.bind("<Button-1>", lambda event, celda=cell: self.on_button_clicked(celda))
    


















