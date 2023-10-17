
import threading
import tkinter as tk
from turtle import width


class LoadingWindow:
    def __init__(self, root):
        self.root=root
        self.root.title("Cargando...")
        self.root.geometry("170x120")
        self.root.resizable(False, False)

        self.label=tk.Label(self.root, text="Cargando datos...", font=("Arial", 14))
        self.label.pack(side=tk.TOP, pady=10)

        label_bg_color=self.label.cget("bg")

        self.canvas=tk.Canvas(self.root, width=60, height=60, bg=label_bg_color) #se instancia un canvas del mismo color de background que el label
        self.canvas.pack()

        self.progress=0

        # Me parece redundante, ya dibujo el circulo en update
        #self.draw_progress_circle(self.progress)

        self.update_progress_circle()

        #self.thread=threading.Thread(target=self.fetch_json_data)
        #self.thread.start()
    
    def draw_progress_circle(self, progress):
        self.canvas.delete("progress")
        angle=int(-360*(progress/100)) # El signo - para que gire en sentido horario
        self.canvas.create_arc(10, 10, 35, 35, 
                               start=90, extent=angle, tags="progress", outline='green', width=4, style=tk.ARC) # start=90 para empezar arriba en lugar de a la derecha
        
    def update_progress_circle(self):
        self.draw_progress_circle(self.progress)
        
        if self.progress<90:
            self.progress+=10
        elif self.progress==90: #La forma mas simple que se me ocurrio de dar el efecto
            self.progress+=9
        else:
            self.progress=0
        
        self.root.after(100, self.update_progress_circle) #se llama a la funcion update_progress_circle desde ella misma: el circulo se dibuja recursivamente

