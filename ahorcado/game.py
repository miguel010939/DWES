import tkinter as tk
from tkinter import messagebox
import load_data


class GameWindow:
    def __init__(self, root, difficulty):
        self.difficulty = difficulty
        self.root = root
        self.root.title("Juego del Ahorcado")

        load_the_data = load_data.LoadData()
        # espera la finalizacion de los hilos
        while not (load_the_data.finished1 and load_the_data.finished2):
            self.root.after(100)

        self.word = load_the_data.random_word(self.difficulty)

        self.mistakes = 0
        #self.word = "palabra"
        self.guessed_word = "_" * self.word.__len__()
        self.used_letters = []
        self.game_done = False
        self.game_won = False

        # image_paths = []
        # image_list = [for url in image_paths]


        self.welcome = tk.Label(self.root, text="¡BIENVENIDO AL JUEGO DEL AHORCADO!\nAdivina una letra de la palabra",
                                font=("Arial", 15))
        self.welcome.pack()

        self.frame = tk.Frame(self.root)
        self.frame.pack()

        self.frame2 = tk.Frame(self.root)
        self.frame2.pack()
        # self.hangman = tk.Label(self.frame2, image=)
        # self.hangman.pack()

        self.guessed_word_label = tk.Label(self.frame2, text=self.guessed_word.upper(), font=("Arial Black", 14))
        self.guessed_word_label.pack(side=tk.LEFT)
        self.mistakes_label = tk.Label(self.frame2, anchor="e", text=str(self.mistakes) + "/6 ERRORES",
                                       font=("Arial", 11))
        self.mistakes_label.pack(padx=10, side=tk.RIGHT)

        self.used_letters_label = tk.Label(self.root, text="Letras ya usadas: " + " ".join(self.used_letters),
                                           font=("Arial", 13))
        self.used_letters_label.pack(pady=7)

        self.frame3 = tk.Frame(self.root)
        self.frame3.pack()
        self.entry = tk.Entry(self.frame3, font=("Arial Black", 14))
        self.entry.pack()
        self.button_guess = tk.Button(self.frame3, text="Adivina", command=self.guess)
        self.button_guess.pack()

    def update_gui(self):
        self.guessed_word_label.config(text=self.guessed_word.upper())
        self.used_letters_label.config(text="Letras ya usadas: " + " ".join(self.used_letters))
        self.mistakes_label.config(text=str(self.mistakes) + "/6 ERRORES")
        self.entry.delete(0, tk.END)
        # Actualiza tambien imagen aqui

    def check_result(self):
        if self.mistakes >= 6:
            self.game_done = True
        elif self.guessed_word == self.word:
            self.game_won = True

        if self.game_won:
            messagebox.showinfo(title="Victoria",
                                message="¡Enhorabuena!\n\n¡Has ganado la partida!\n\nLa palabra correcta es: " + self.word.upper())
            self.root.destroy()
        elif self.game_done:
            messagebox.showinfo(title="Derrota",
                                message="¡Lástima!\n\nHas perdido...\n\nLa palabra correcta era: " + self.word.upper())
            self.root.destroy()

    def guess(self):
        guessed = False
        if self.entry.get().isalpha():
            # despues de comprobar que la entrada es alfabetica, se toma la primera letra en minusculas como input
            letter = self.entry.get().lower()[0]
            # creo una lista, porque string no tiene setter
            updated_word = [letra for letra in self.guessed_word]
            for i in range(len(self.word)):
                if self.word[i] == letter:  # compruebo letra a letra
                    guessed = True
                    updated_word[i] = letter  # en caso de haber acertado, actualizo letra a letra
            self.guessed_word = "".join(updated_word)
            if not guessed:
                # si no se ha acertado, incremento el contador de errores y añado la letra a la lista de usadas
                self.mistakes += 1
                if letter not in self.used_letters:
                    self.used_letters.append(letter)
        else:
            messagebox.showerror(title="Error de entrada",
                                 message="Sólo se admiten letras.\nNi números ni caracteres especiales")
        self.update_gui()
        self.check_result()


if __name__ == '__main__':
    root_main = tk.Tk()
    app = GameWindow(root_main, 0)
    root_main.mainloop()
