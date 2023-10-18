import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class DetailWindow:

    def __init__(self, root, title, image, description):
        self.root=root
        self.title= title
        self.image=image
        self.description=description

        x=(self.root.winfo_screenwidth() - self.root.winfo_reqwidth())/2
        y=(self.root.winfo_screenheight() - self.root.winfo_reqheight())/2
        self.root.geometry(f"+{int(x)}+{int(y)}")

        self.window=tk.Toplevel(root)
        self.window.title(self.title)

        title_label=ttk.Label(self.window, text=self.title)
        title_label.pack() # cambie el orden de los pack() para que el titulo apareciese encima de la imagen

        image_label=ttk.Label(self.window, image=self.image)
        image_label.pack(pady=7) # y le anhadi algo de padding a la imagen
        

        description_label=ttk.Label(self.window, text=self.description, wraplength=300)
        description_label.pack()

    
   


