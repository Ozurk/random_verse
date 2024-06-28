from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scatter import Scatter
import random
from kivy.properties import ListProperty
import shutil
import os

class RandomDev(BoxLayout):


    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.chosen_text = None
        self.chosen_book = None
        self.chosen_chapter = None

    def get_random_scripture(self):
        number_of_books = None
        index = 0
        folder_path = "The Bible by Chapter"
        def count_subfolders(thebiblebychapter):
            try:
                subfolders = next(os.walk(folder_path))[1]

                return len(subfolders)




class RandomDevApp(App):
    def build(self):
        return RandomDev()


if __name__ == '__main__':
    app = RandomDevApp()
    app.run()
