from tkinter import ttk, Tk
import tkinter as tk
from cell import Cell
from tkinter import messagebox
from detail_window import DetailWindow

class MainWindow():
    def on_button_clicked(self, cell):
        
        #root_detail = Tk()
        DetailWindow(self.root, cell.title, cell.image, cell.description)
        #root_detail.mainloop()

    
    def __init__(self, root):

        self.root=root
        root.title("MainWindow")

        self.cells=[
            Cell("Animal 1", ".\\data\\unedited\\07CAT-STRIPES-mediumSquareAt3X-v2.jpg", "This is a tabby cat. I think it's quite cute"),
            Cell("Animal 2", ".\\data\\unedited\\arctic_fox.jpg", "This is an artic fox... Definitely the cutest"),
            Cell("Animal 3", ".\\data\\unedited\\brown_bear.jpg"),
            Cell("Animal 4", ".\\data\\unedited\\koala.jpg", "This is a koala, one of the many species endemic to Australia"),
            Cell("Animal 5", ".\\data\\unedited\\red_panda.jpg", "This is a red panda. Despite the name, it's not a species of bear. Most of them live in China and the Himalayas")
        ]
        for i, cell in enumerate(self.cells):
            label=ttk.Label(root, image=cell.image, text=cell.title, compound=tk.BOTTOM)
            label.grid(row=0, column=i)
            label.bind("<Button-1>", lambda event, cell=cell: self.on_button_clicked(cell))
    


















