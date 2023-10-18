from window import MainWindow
import threading
import requests
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

        self.json_data=[] # El atributo json_data es para almacenar y usar fuera del thread la info del json descargado
        self.finished=False # Determina si la ejecucion del thread ha finalizado

        self.thread=threading.Thread(target=self.fetch_json_data)
        self.thread.start()

        self.check_thread() # Comprueba que termino la ejecucion del hilo para lanzar la ventana con los datos descargados. Si se comenta esta linea se aprecia mejor lo bonita que quedo la ventana de carga

    def fetch_json_data(self):
        response = requests.get("https://raw.githubusercontent.com/miguel010939/DWES/main/recursos/catalog.json")
        if response.status_code == 200:
            json_data = response.json()
            #print(json_data)
            #self.launch_main_window(json_data) # Daba error porque no se puede modificar la interfaz en un hilo. Esta funcion llamaba a MainWindow()
            self.json_data=json_data # Se guardan los datos en el atributo del objeto
            self.finished = True # Termino la ejecucion del hilo
    
    def check_thread(self):
        if self.finished:
            self.root.destroy() # Cierra ventana de carga
            self.launch_main_window(self.json_data) # Instancia la ventana principal con los datos del json descargado
        else:
            self.root.after(100, self.check_thread)


    def launch_main_window(self, json_data):
        root = tk.Tk()
        app = MainWindow(root, json_data)
        root.mainloop()

    
    def draw_progress_circle(self, progress):
        self.canvas.delete("progress")
        angle=int(-360*(progress/100)) # El signo - para que gire en sentido horario
        self.canvas.create_arc(10, 10, 35, 35, 
                               start=90, extent=angle, tags="progress", outline='teal', width=4, style=tk.ARC) # start=90 para empezar arriba en lugar de a la derecha
        
    def update_progress_circle(self):
        self.draw_progress_circle(self.progress)
        
        if self.progress<90:
            self.progress+=10
        elif self.progress==90: #La forma mas simple que se me ocurrio de dar el efecto
            self.progress+=9
        else:
            self.progress=0
        
        self.root.after(100, self.update_progress_circle) #se llama a la funcion update_progress_circle desde ella misma: el circulo se dibuja recursivamente

