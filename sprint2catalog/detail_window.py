import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class DetailWindow:

    def __init__(self, root, title, image, description):
        self.root=root
        self.title= title
        self.image=image
        self.description=description

        
        #self.window=tk.Toplevel(root)
        #self.window.title(self.title)

        # Sustitui window por root para que asocie el contenido a la ventana toplevel creada en window.on_button_clicked()

        title_label=ttk.Label(self.root, text=self.title)
        title_label.pack() # cambie el orden de los pack() para que el titulo apareciese encima de la imagen

        image_label=ttk.Label(self.root, image=self.image)
        image_label.pack(pady=7) # y le anhadi algo de padding a la imagen
        

        description_label=ttk.Label(self.root, text=self.description, wraplength=300)
        description_label.pack()

        #self.root.geometry(f"{self.dim_x}x{self.dim_y}")
        self.root.update_idletasks()
        self.x=(self.root.winfo_screenwidth() - self.root.winfo_reqwidth())/2 # La diferencia entre la anchura de la pantalla y la ventana se reparte la mitad a cada lado -> centrado
        self.y=(self.root.winfo_screenheight() - self.root.winfo_reqheight())/2 # Analogo
        #print("x: "+str(self.x))
        #print("y: "+str(self.y))
    
        self.root.geometry(f"+{int(self.x)}+{int(self.y)}")


       


    
   


