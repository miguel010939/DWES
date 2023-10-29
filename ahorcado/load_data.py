import threading
import requests
import random
from PIL import Image, ImageTk
from io import BytesIO


class LoadData:
    def __init__(self):

        self.json = {}
        self.finished1 = False
        self.thread1 = threading.Thread(target=self.fetch_json)

        self.images = {}
        self.finished2 = False
        self.thread2 = threading.Thread(target=self.fetch_images)

        # carga los datos al instanciar un objeto de la clase
        self.thread1.start()
        self.thread2.start()

    def fetch_json(self):
        response = requests.get("https://raw.githubusercontent.com/miguel010939/DWES/main/ahorcado/data/dict/dictionary.json")
        if response.status_code == 200:
            self.json = response.json()
            #print(self.json)
            self.finished1 = True

    def fetch_images(self):
        response = requests.get("https://raw.githubusercontent.com/miguel010939/DWES/main/ahorcado/data/dict/hangman_images.json")
        if response.status_code == 200:
            self.images = response.json()
            #print(self.images)
            self.finished2 = True

    def get_images(self):
        image_list = [ImageTk.PhotoImage(Image.open(BytesIO(requests.get(path).content))) for path in self.images.get("hangman_sequence")]
        return image_list

    def random_word(self, difficulty):
        word_list = self.json.get(str(difficulty))
        word = random.choice(word_list)
        return word
