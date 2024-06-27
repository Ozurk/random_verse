from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout


class RandomDev(BoxLayout):
    pass


class RandomDevApp(App):
    def build(self):
        return RandomDev()


if __name__ == '__main__':
    app = RandomDevApp()
    app.run()
