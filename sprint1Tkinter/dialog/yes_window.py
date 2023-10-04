from tkinter import ttk, Tk

class YesWindow:
    def __init__(self, root):
        self.root=root

        label_yes = ttk.Label(root, text="Por supesto!")
        label_yes.pack()