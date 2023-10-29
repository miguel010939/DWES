import tkinter as tk
from game import GameWindow


class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Menú Principal")
        self.root.resizable(False, False)

        # centra la ventana
        self.x = (self.root.winfo_screenwidth() - self.root.winfo_reqwidth()) / 2
        self.y = (self.root.winfo_screenheight() - self.root.winfo_reqheight()) / 2
        self.root.geometry(f"+{int(self.x)}+{int(self.y)}")

        self.label = tk.Label(self.root, text="Elige dificultad", font=("Arial Black", 11))
        self.label.pack(side=tk.TOP)

        # para agrupar los botones de seleccion de dificultad
        self.frame = tk.Frame(self.root, borderwidth=2)
        self.frame.pack(pady=5)

        self.button_easy = tk.Button(self.frame, text="Fácil", width=15, command=self.start_easy_game)
        self.button_easy.pack(pady=3)
        self.button_normal = tk.Button(self.frame, text="Normal", width=15, command=self.start_normal_game)
        self.button_normal.pack(pady=3)
        self.button_difficult = tk.Button(self.frame, text="Difícil", width=15, command=self.start_difficult_game)
        self.button_difficult.pack(pady=3)

        self.label = tk.Label(self.root, text="O sal del juego", font=("Arial Black", 11))
        self.label.pack()

        self.button_exit = tk.Button(self.root, text="Salir", width=10, command=self.exit_game)
        self.button_exit.pack()

    def start_easy_game(self):
        self.start_game(0)

    def start_normal_game(self):
        self.start_game(1)

    def start_difficult_game(self):
        self.start_game(2)

    def start_game(self, difficulty):
        root_game = tk.Toplevel()
        game = GameWindow(root_game, difficulty)
        root_game.mainloop()

    def exit_game(self):
        self.root.destroy()


if __name__ == '__main__':
    root_main = tk.Tk()
    app = MainWindow(root_main)
    root_main.mainloop()
