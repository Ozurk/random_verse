from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scatter import Scatter
import random
from kivy.properties import StringProperty
from kivy.properties import ListProperty
from kivy.graphics import Color, Rectangle
import shutil
import os
import re


def get_file(file_path):
    try:
        file = open(file_path, "r")
        text = file.read()
        text = text.strip()
        file.close()
        return text
    except UnicodeDecodeError:
        file = open(file_path, "r", encoding="utf-8")
        text = file.read()
        text = text.strip()
        file.close()
        return text


class RandomDev(BoxLayout):
    chosen_text = StringProperty("")
    chosen_book = StringProperty("")
    chosen_chapter = StringProperty("")
    chosen_verse = StringProperty("")
    text_color = ListProperty([1, 1, 1, 1])
    click_counter = 0
    click_counter_var = StringProperty("")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def get_random_scripture(self):
        list_of_books = list(os.listdir('Bible'))

        self.chosen_book = list_of_books[random.randint(0, 65)]
        os.chdir(f'Bible/{self.chosen_book}')
        list_of_chapters = list(os.listdir())

        self.chosen_chapter = list_of_chapters[random.randint(0, len(list_of_chapters) - 1)]
        self.chosen_text = get_file(self.chosen_chapter)
        lines = self.chosen_text.splitlines()
        self.chosen_verse = lines[random.randint(1, len(lines) - 1)]
        os.chdir('../')
        os.chdir('../')
        if self.chosen_text == "":
            self.get_random_scripture()
        self.text_color = [random.random() for i in range(3)] + [1]
        self.click_counter += 1
        self.click_counter_var = str(self.click_counter)


class RandomDevApp(App):
    def build(self):
        return RandomDev()


if __name__ == '__main__':
    app = RandomDevApp()
    app.run()
