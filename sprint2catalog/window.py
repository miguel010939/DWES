from tkinter import ttk, Tk
import tkinter as tk
from cell import Cell
from tkinter import messagebox
from detail_window import DetailWindow

class MainWindow:
    def on_button_clicked(self, cell):
        # Creo una ventana toplevel para luego poder centrar en la pantalla la detail_window
        root_detail = tk.Toplevel()
        DetailWindow(root_detail, cell.title, cell.image, cell.description)
        root_detail.mainloop()

    
    def __init__(self, root, json_data):

        self.root=root
        root.title("MainWindow")

        # Mensaje a mostrar al clickar "Acerca de"
        def show_about_window():
            messagebox.showinfo(title="Acerca del desarrollador", 
                                message="Me llamo Alejo, soy el desarrollador\n\nAcerca de Alejo:\n\t- Hoy no ha dormido muy bien\n\t- Le encantan las tostadas con mermelada de moras")


        # Barra de menus
        barra_menus=tk.Menu()
        # Un menu para la barrade menus. Crea otra instancia de tk.Menu
        menu_ayuda = tk.Menu(barra_menus, tearoff=False)
        # Anhade una opcion al menu
        menu_ayuda.add_command(
            label="Acerca de",
            accelerator="Ctrl+A",
            command=show_about_window
        )
        # Agrega el menu creado a la barra de menus
        barra_menus.add_cascade(menu=menu_ayuda, label="Ayuda")
        # Asocia el menu barra_menus a la ventana
        root.config(menu=barra_menus)


        self.root.geometry("200x300")

        self.x=(self.root.winfo_screenwidth() - self.root.winfo_reqwidth())/2
        self.y=(self.root.winfo_screenheight() - self.root.winfo_reqheight())/2
        self.root.geometry(f"+{int(self.x)}+{int(self.y)}")

        self.cells=[]
        for dict in json_data:
            # almacena en variables los datos de cada imagen
            name=dict.get("name")
            path=dict.get("image_url")
            description=dict.get("description")
            cell= Cell(name, path, description) # instancio una celda por cada imagen del json array
            self.cells.append(cell) # la anhado a la lista de celdas


        for i, cell in enumerate(self.cells):
            label=ttk.Label(root, image=cell.image, text=cell.title, compound=tk.BOTTOM)
            label.grid(row=i, column=0)
            label.bind("<Button-1>", lambda event, cell=cell: self.on_button_clicked(cell))
    


















