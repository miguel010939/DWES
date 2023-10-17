from tkinter import Tk
from window import MainWindow
from loading_window import LoadingWindow

if __name__ == "__main__":
    root=Tk()
    app=LoadingWindow(root)
    root.mainloop()
    