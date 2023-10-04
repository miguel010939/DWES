from tkinter import ttk, Tk

class NoWindow:
    def __init__(self, root):
        self.root=root

        label_no = ttk.Label(root, text="Claro que no!")
        label_no.pack()