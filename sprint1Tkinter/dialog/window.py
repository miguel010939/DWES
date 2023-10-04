from tkinter import ttk, Button, Tk
from yes_window import YesWindow
from no_window import NoWindow

class MainWindow:
    def on_yes_button_click(self):
        yeswindow_root=Tk()
        app=YesWindow(yeswindow_root)
        yeswindow_root.mainloop()

    def on_no_button_click(self):
        nowindow_root=Tk()
        app=NoWindow(nowindow_root)
        nowindow_root.mainloop()

    def __init__(self, root):
        self.root=root

        frame = ttk.Frame(self.root)
        frame.pack()

        label_dilemma = ttk.Label(frame, text="Dilema trascendental...")
        label_dilemma.pack()


        button_yes=ttk.Button(frame, text="Sí", command= self.on_yes_button_click)
        button_yes.pack(side="left")

        button_no=ttk.Button(frame, text="No", command= self.on_no_button_click)
        button_no.pack(side="right")


        
