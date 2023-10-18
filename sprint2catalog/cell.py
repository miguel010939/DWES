from http.client import REQUESTED_RANGE_NOT_SATISFIABLE
import tkinter as tk
from tkinter import Tk
from PIL import Image, ImageTk
from io import BytesIO
import requests
from detail_window import DetailWindow

class Cell:
     
    def __init__(self, title, path, description="No description available"):
        self.title=title
        self.path=path
        self.description=description
        
        self.load_image_from_url(self.path)

    def load_image_from_url(self, url):
        response = requests.get(url)
        img_data = Image.open(BytesIO(response.content))
        self.image = ImageTk.PhotoImage(img_data)